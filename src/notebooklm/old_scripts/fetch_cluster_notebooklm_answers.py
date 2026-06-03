#!/usr/bin/env python3
"""Fetch NotebookLM-backed cluster synthesis notes."""

import argparse
import json
import re
import subprocess
import sys
import tempfile
import time
from datetime import date
from pathlib import Path

NOTEBOOK_ID = "3d5d829d-98cc-463b-a919-2a8e266344fb"
EVIDENCE_MAP_PATH = Path("02_LitRev_Sistematica/derived/cluster_evidence_map.json")


def load_json(path: str | Path) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def json_frontmatter_value(value) -> str:
    return json.dumps(value, ensure_ascii=False)


def cluster_questions(registry: dict) -> list[dict]:
    questions = registry.get("cluster_questions")
    if not questions:
        raise SystemExit(
            "No machine-readable cluster_questions section found in registry. "
            "Run the registry extraction step or inspect 04_Cluster_Questions in the Excel registry."
        )
    return questions


def existing_note_complete(path: Path) -> bool:
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8")
    return "[NOTEBOOKLM_CLUSTER]" in text and re.search(r'^status:\s*"?draft"?', text, re.M) is not None


def select_questions(all_questions: list[dict], only: str | None, limit: int | None, output_dir: Path, overwrite: bool) -> list[dict]:
    selected = all_questions
    if only:
        wanted = {x.strip() for x in only.split(",") if x.strip()}
        selected = [q for q in all_questions if q["cluster_question_id"] in wanted or q["question_id"] in wanted]
    else:
        selected = [
            q
            for q in all_questions
            if overwrite or not existing_note_complete(output_dir / f"{q['cluster_question_id']}.md")
        ]
    if limit is not None:
        selected = selected[:limit]
    return selected


def evidence_for_cluster(evidence_map: dict, cluster_id: str) -> dict:
    return evidence_map.get(cluster_id, {"notes": [], "source_ids": [], "source_titles": []})


def trim(text: str, limit: int = 700) -> str:
    clean = re.sub(r"\s+", " ", text or "").strip()
    return clean[:limit] + ("..." if len(clean) > limit else "")


def build_prompt(q: dict, evidence: dict) -> str:
    note_ids = ", ".join(note["note_id"] for note in evidence.get("notes", []))

    return f"""Answer this cluster-level literature synthesis question for a Fondecyt project on land-rent financialization.

Use only the selected NotebookLM source papers.
Do not rely on prior chat history. Preserve citations/page anchors where available.
Do not fabricate details. Mark uncertain Latin American applications as requiring verification.

Cluster: {q['cluster_id']} - {q['cluster_name']}
Question: {q['question_text']}
Related source IDs: {', '.join(q['related_source_ids'])}
Related Phase 1 note IDs for local cross-checking: {note_ids}

Return a concise synthesis with citations. Cover:
1. the cross-paper answer,
2. key mechanisms and variables,
3. tensions, limits, and open questions,
4. relevance to the final 5-15 page memo.
"""


def run_notebooklm(prompt: str, source_ids: list[str], source_map: dict, timeout: int, new_chat: bool) -> dict:
    cmd = ["notebooklm", "ask", "--json", "--notebook", NOTEBOOK_ID, "--timeout", str(timeout)]
    if new_chat:
        cmd.extend(["--new", "--yes"])
    for sid in source_ids:
        mapped = source_map.get(sid)
        if mapped:
            cmd.extend(["--source", mapped])

    with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".txt", delete=False) as f:
        f.write(prompt)
        prompt_path = f.name

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
        message = proc.stderr.strip() or proc.stdout.strip()
        if "Authentication expired" in message or "Run 'notebooklm login'" in message:
            raise RuntimeError("NotebookLM authentication expired. Run: notebooklm login")
        raise RuntimeError(message)
    return json.loads(proc.stdout)


def run_notebooklm_with_retry(prompt: str, source_ids: list[str], source_map: dict, timeout: int, new_chat: bool) -> dict:
    last_error = None
    for attempt in range(1, 4):
        try:
            return run_notebooklm(prompt, source_ids, source_map, timeout, new_chat)
        except RuntimeError as exc:
            last_error = exc
            if "No parseable chunks" not in str(exc) and "response was empty" not in str(exc):
                raise
            time.sleep(5 * attempt)
    raise last_error


def section(answer: str, heading: str, next_heading: str | None = None) -> str:
    if next_heading:
        pattern = rf"{re.escape(heading)}\s*(.*?)(?=\n{re.escape(next_heading)}|\Z)"
    else:
        pattern = rf"{re.escape(heading)}\s*(.*)"
    match = re.search(pattern, answer, re.S)
    return match.group(1).strip() if match else ""


def source_table_from_evidence(evidence: dict) -> str:
    rows = ["| Source ID | Paper | Mechanism / claim | Evidence anchor | Relevance |", "| --------- | ----- | ----------------- | --------------- | --------- |"]
    by_source: dict[str, list[dict]] = {}
    for note in evidence.get("notes", []):
        by_source.setdefault(note["source_id"], []).append(note)
    for sid, notes in by_source.items():
        paper = notes[0]["paper_title"]
        claim = trim(" ".join(n.get("distilled_note", "") for n in notes), 220).replace("|", "/")
        anchor = trim(" ".join(n.get("evidence_page_anchors", "") for n in notes), 180).replace("|", "/")
        links = ", ".join(f"[[{n['note_id']}]]" for n in notes)
        rows.append(f"| {sid} | {paper} | {claim} | {anchor} | {links} |")
    return "\n".join(rows)


def memo_relevance(question_text: str, cluster_name: str) -> list[str]:
    text = f"{question_text} {cluster_name}".lower()
    labels = []
    if "overvaluation" in text or "unbalanced" in text:
        labels.append("land overvaluation theorem")
    if "credit" in text or "crowd" in text or "collateral" in text:
        labels.append("land-credit crowding-out")
    if "debt" in text or "rollover" in text or "r versus g" in text or "r<g" in text:
        labels.append("debt rollover / R versus G")
    if "wobbly" in text or "phase" in text or "instability" in text or "fluctuation" in text:
        labels.append("wobbly dynamics and instability")
    if "tax" in text or "policy" in text or "regulation" in text:
        labels.append("policy / taxation / regulation")
    if "latin" in text or "applicability" in text or "peripheral" in text:
        labels.append("Latin American applicability")
    return labels or ["Latin American applicability"]


def render_note(q: dict, evidence: dict, notebooklm_source_ids: list[str], answer: str) -> str:
    today = date.today().isoformat()
    related_notes = evidence.get("per_paper_note_ids") or [n["note_id"] for n in evidence.get("notes", [])]
    answer_table = section(answer, "## Cross-paper evidence map", "## Synthesis note")
    synthesis = section(answer, "## Synthesis note", "## Tensions, limits, and open questions")
    tensions = section(answer, "## Tensions, limits, and open questions", "## Memo relevance")
    memo = section(answer, "## Memo relevance")
    labels = memo_relevance(q["question_text"], q["cluster_name"])

    table = answer_table if "| Source ID | Paper |" in answer_table else source_table_from_evidence(evidence)
    links = "\n".join(f"- [[{note_id}]]" for note_id in related_notes)

    return f"""---
type: literature_cluster_note
status: draft
phase: 2_cluster_synthesis
cluster_id: {json_frontmatter_value(q['cluster_id'])}
cluster_name: {json_frontmatter_value(q['cluster_name'])}
question_id: {json_frontmatter_value(q['question_id'])}
cluster_question_id: {json_frontmatter_value(q['cluster_question_id'])}
question_text: {json_frontmatter_value(q['question_text'])}
related_source_ids: {json_frontmatter_value(q['related_source_ids'])}
related_paper_titles: {json_frontmatter_value(q['related_paper_titles'])}
related_per_paper_notes: {json_frontmatter_value(related_notes)}
notebooklm_source_ids: {json_frontmatter_value(notebooklm_source_ids)}
created_from_registry: true
notebooklm_backed: true
created: {json_frontmatter_value(today)}
updated: {json_frontmatter_value(today)}
---
# {q['cluster_question_id']} — {q['cluster_name']}

> [!question]
> {q['question_text']}

## Cluster scope

- Cluster: `{q['cluster_id']}` — {q['cluster_name']}
- Related sources: {", ".join(q['related_source_ids'])}
- Related papers: {"; ".join(q['related_paper_titles'])}
- Evidence map: `02_LitRev_Sistematica/derived/cluster_evidence_map.json`

## NotebookLM answer

[NOTEBOOKLM_CLUSTER]

{answer.strip()}

## Cross-paper evidence map

{table}

## Synthesis note

{synthesis or "See the NotebookLM answer and evidence map above for the structured synthesis."}

## Tensions, limits, and open questions

{tensions or "Review the source-specific caveats and unresolved assumptions before using this synthesis as final memo prose."}

## Links to related notes

{links}

## Memo relevance

- Relevance class: {", ".join(labels)}

{memo or "This note supports the Phase 3 cross-cluster synthesis for the 5-15 page Fondecyt working memo."}
"""


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch NotebookLM cluster synthesis notes.")
    parser.add_argument("--limit", type=int)
    parser.add_argument("--only", help="Comma-separated cluster question IDs, e.g. C1_Q01,C2_Q03")
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--new-chat", action="store_true", default=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--source-map", default="02_LitRev_Sistematica/config/notebooklm_source_map.json")
    parser.add_argument("--registry", default="02_LitRev_Sistematica/config/registry_parsed.json")
    parser.add_argument("--output-dir", default="notes/clusters")
    parser.add_argument("--timeout", type=int, default=240)
    args = parser.parse_args()

    registry = load_json(args.registry)
    source_map = load_json(args.source_map)
    evidence_map = load_json(EVIDENCE_MAP_PATH) if EVIDENCE_MAP_PATH.exists() else {}
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    selected = select_questions(cluster_questions(registry), args.only, args.limit, output_dir, args.overwrite)
    if args.dry_run:
        for q in selected:
            notebooklm_ids = [source_map.get(sid, "") for sid in q["related_source_ids"] if source_map.get(sid)]
            print(f"{q['cluster_question_id']}: {q['question_text']} | sources={q['related_source_ids']} | notebooklm={notebooklm_ids}")
        return

    for q in selected:
        out = output_dir / f"{q['cluster_question_id']}.md"
        if out.exists() and not args.overwrite:
            print(f"Skipping existing note without --overwrite: {out}", file=sys.stderr)
            continue
        evidence = evidence_for_cluster(evidence_map, q["cluster_id"])
        notebooklm_ids = [source_map[sid] for sid in q["related_source_ids"] if sid in source_map]
        print(f"Asking NotebookLM cluster question: {q['cluster_question_id']} - {q['question_text']}", file=sys.stderr)
        response = run_notebooklm_with_retry(build_prompt(q, evidence), q["related_source_ids"], source_map, args.timeout, args.new_chat)
        out.write_text(render_note(q, evidence, notebooklm_ids, response.get("answer", "")), encoding="utf-8")
        print(f"Saved {out}")


if __name__ == "__main__":
    main()
