#!/usr/bin/env python3
"""Fetch answers from NotebookLM and save per-question Obsidian notes.

Prerequisites:
  notebooklm login
  notebooklm auth check --test --json

Examples:
  python scripts/fetch_notebooklm_answers.py --notebook NOTEBOOK_ID --limit 3
  python scripts/fetch_notebooklm_answers.py --notebook NOTEBOOK_ID --only PDF002_Q06
  python scripts/fetch_notebooklm_answers.py --notebook NOTEBOOK_ID --source-map config/source_map.json
"""

import argparse
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

REGISTRY_PATH = Path("02_LitRev_Sistematica/config/registry_parsed.json")
NOTES_DIR = Path("notes/questions")


def frontmatter_status(path: Path) -> str | None:
    if not path.exists():
        return None
    text = path.read_text(encoding="utf-8")
    if text.startswith('"---\\n'):
        text = decode_escaped_markdown(text)
    match = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return None
    status_match = re.search(r'^status:\s*"?([^"\n]+)"?', match.group(1), re.MULTILINE)
    return status_match.group(1).strip() if status_match else None


def decode_escaped_markdown(text: str) -> str:
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        if text.startswith('"') and text.endswith('"'):
            text = text[1:-1]
        return text.replace("\\n", "\n").replace('\\"', '"')


def is_completed(question_id: str) -> bool:
    return frontmatter_status(NOTES_DIR / f"{question_id}.md") == "draft"


def load_questions() -> list[dict]:
    data = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    return data["questions"]


def referenced_source_ids(q: dict) -> list[str]:
    source_ids = [q["source_id"]]
    for source_id in re.findall(r"\bPDF\d{3}\b", q["question_text"] or ""):
        if source_id not in source_ids:
            source_ids.append(source_id)
    return source_ids


def build_prompt(q: dict) -> str:
    source_list = ", ".join(referenced_source_ids(q))
    return f"""You are answering one source-grounded literature-review extraction question.

Do not rely on prior chat history in this notebook. If relevant context is not
present in the selected source, say that it requires external verification.
For project-memo, Fondecyt, Latin America, translation, or critique questions,
use the project context stated in the question as the task frame and infer from
the selected source. Do not refuse merely because the source does not mention
the project, Fondecyt, or Latin America by name.

Use only the selected NotebookLM source(s) corresponding to:
- Source ID(s): {source_list}
- Paper title: {q['paper_title']}
- Authors: {q['authors']}

Question:
{q['question_text']}

Return concise scholarly content in this exact structure:

NotebookLM answer:
[One paragraph answering the question, with citations if available.]

Distilled note:
- Core claim: [1-2 sentences]
- Mechanism:
  - [causal step 1]
  - [causal step 2]
  - [causal step 3]
  - [causal step 4 if useful]
- Formal object/result, if any: [theorem/proposition/equation, or "Not applicable"]
- Relevance for the project memo: [land-price inflation, credit crowding-out, land overvaluation, debt rollover, or critique]
- Critical caveat: [Latin American applicability caveat]

Evidence / page anchors:
- Page(s): [page numbers if NotebookLM provides them; otherwise UNKNOWN]
- Key passage(s), paraphrased or short quote only: [short evidence anchor, no long quotation]
"""


def ask_notebooklm(q: dict, notebook_id: str, source_map: dict[str, str], timeout: int, new_chat: bool) -> dict:
    cmd = ["notebooklm", "ask", "--json", "--notebook", notebook_id, "--timeout", str(timeout)]
    if new_chat:
        cmd.extend(["--new", "--yes"])

    for source_id in referenced_source_ids(q):
        notebooklm_source_id = source_map.get(source_id)
        if notebooklm_source_id:
            cmd.extend(["--source", notebooklm_source_id])

    with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".txt", delete=False) as prompt_file:
        prompt_file.write(build_prompt(q))
        prompt_path = prompt_file.name

    try:
        proc = subprocess.run(
            cmd + ["--prompt-file", prompt_path],
            check=False,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
    finally:
        Path(prompt_path).unlink(missing_ok=True)

    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip())

    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"NotebookLM returned non-JSON output: {proc.stdout[:500]}") from exc


def section_value(text: str, start: str, end: str | None = None) -> str:
    pattern = rf"{re.escape(start)}\s*(.*)"
    if end:
        pattern = rf"{re.escape(start)}\s*(.*?)(?={re.escape(end)})"
    match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
    return match.group(1).strip() if match else ""


def normalize_distilled(answer: str) -> str:
    distilled = section_value(answer, "Distilled note:", "Evidence / page anchors:")
    if not distilled:
        return (
            "- **Core claim**: [NEEDS_VERIFICATION]\n"
            "- **Mechanism**:\n"
            "  - [NEEDS_VERIFICATION]\n"
            "- **Formal object/result, if any**: [NEEDS_VERIFICATION]\n"
            "- **Relevance for the project memo**: [NEEDS_VERIFICATION]\n"
            "- **Critical caveat**: [NEEDS_VERIFICATION]"
        )

    replacements = {
        "- Core claim:": "- **Core claim**:",
        "- Mechanism:": "- **Mechanism**:",
        "- Formal object/result, if any:": "- **Formal object/result, if any**:",
        "- Relevance for the project memo:": "- **Relevance for the project memo**:",
        "- Critical caveat:": "- **Critical caveat**:",
    }
    for old, new in replacements.items():
        distilled = distilled.replace(old, new)
    return distilled


def normalize_evidence(answer: str, references: list[dict]) -> tuple[str, str]:
    evidence = section_value(answer, "Evidence / page anchors:")
    page_match = re.search(r"Page\(s\):\s*(.*)", evidence, re.IGNORECASE)
    passage_match = re.search(r"Key passage\(s\).*?:\s*(.*)", evidence, re.IGNORECASE | re.DOTALL)

    pages = page_match.group(1).strip() if page_match else "`[UNKNOWN]`"
    passage = passage_match.group(1).strip() if passage_match else ""

    if not passage and references:
        snippets = []
        for ref in references[:3]:
            cited = (ref.get("cited_text") or "").strip().replace("\n", " ")
            if cited:
                snippets.append(cited[:240])
        passage = " / ".join(snippets)

    return pages or "`[UNKNOWN]`", passage or "[NEEDS_VERIFICATION]"


def render_note(q: dict, response: dict) -> str:
    raw_answer = (response.get("answer") or "").strip()
    answer_only = section_value(raw_answer, "NotebookLM answer:", "Distilled note:") or raw_answer
    pages, passage = normalize_evidence(raw_answer, response.get("references") or [])

    return f"""---
note_id: "{q['question_id']}"
note_type: "notebooklm_per_paper_question"
status: "draft"
source_id: "{q['source_id']}"
question_id: "{q['question_id']}"
paper_title: "{q['paper_title']}"
authors: "{q['authors']}"
year: {int(q['year'])}
venue: "{q['venue']}"
cluster_id: "{q['cluster_id']}"
cluster_name: "{q['cluster_name']}"
question_tag: "{q['tag']}"
use: "NotebookLM answer; then paste distilled note into Obsidian"
---
# {q['question_id']}

## Source

- Source ID: `{q['source_id']}`
- Paper: {q['paper_title']}
- Authors: {q['authors']}
- Year: {int(q['year'])}
- Venue/status: {q['venue']}
- Cluster: `{q['cluster_id']}`

## NotebookLM question

{q['question_text']}

## NotebookLM answer

> [NOTEBOOKLM] {answer_only}

## Distilled note

{normalize_distilled(raw_answer)}

## Evidence / page anchors

- Page(s): {pages}
- Key passage(s), paraphrased or short quote only: {passage}

## Links

- Source paper note: [[{q['source_id']}]]
- Cluster note: [[{q['cluster_id']}]]
- Question index: [[I02_per_paper_question_index#{q['question_id']}]]

## Next action

- [ ] Run/paste NotebookLM answer [if pending]
- [ ] Distill answer [if not done]
- [ ] Add evidence anchors [if missing]
- [ ] Link to cluster synthesis [defer until Phase 2]
"""


def main() -> None:
    parser = argparse.ArgumentParser(description="Ask NotebookLM for unanswered notes.")
    parser.add_argument("--notebook", required=True, help="NotebookLM notebook ID.")
    parser.add_argument("--limit", type=int, default=3, help="Maximum questions to fetch.")
    parser.add_argument("--only", action="append", default=[], help="Specific question ID to fetch. Repeatable.")
    parser.add_argument("--source-map", type=Path, help="Optional JSON map from PDFXXX to NotebookLM source ID.")
    parser.add_argument("--timeout", type=int, default=120, help="NotebookLM request timeout in seconds.")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite completed draft notes.")
    parser.add_argument(
        "--new-chat",
        action="store_true",
        help="Start a fresh NotebookLM chat for each question. Clears notebook chat history, not sources.",
    )
    args = parser.parse_args()

    source_map = {}
    if args.source_map:
        source_map = json.loads(args.source_map.read_text(encoding="utf-8"))

    questions = load_questions()
    if args.only:
        wanted = set(args.only)
        batch = [q for q in questions if q["question_id"] in wanted]
    else:
        batch = [q for q in questions if args.overwrite or not is_completed(q["question_id"])][: args.limit]

    if not batch:
        print("No pending questions found.")
        return

    NOTES_DIR.mkdir(parents=True, exist_ok=True)
    for q in batch:
        print(f"Asking NotebookLM: {q['question_id']} - {q['question_text']}", file=sys.stderr)
        response = ask_notebooklm(q, args.notebook, source_map, args.timeout, args.new_chat)
        output_path = NOTES_DIR / f"{q['question_id']}.md"
        output_path.write_text(render_note(q, response), encoding="utf-8")
        print(f"Saved {output_path}")


if __name__ == "__main__":
    main()
