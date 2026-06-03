#!/usr/bin/env python3
"""Print the next unanswered per-paper questions.

State is inferred from files in notes/questions instead of a hard-coded
last-completed ID. A note counts as complete when its frontmatter status is
"draft"; pending templates are ignored.
"""

import argparse
import json
import re
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


def main() -> None:
    parser = argparse.ArgumentParser(description="Show the next unanswered registry questions.")
    parser.add_argument("--limit", type=int, default=5, help="Number of questions to print.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    args = parser.parse_args()

    data = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    pending = [q for q in data["questions"] if not is_completed(q["question_id"])]
    batch = pending[: args.limit]

    if args.json:
        print(json.dumps({"count": len(batch), "questions": batch}, indent=2, ensure_ascii=False))
        return

    for q in batch:
        print(f"ID: {q['question_id']}")
        print(f"Text: {q['question_text']}")
        print(f"Tag: {q['tag']}")
        print(f"Status: {frontmatter_status(NOTES_DIR / (q['question_id'] + '.md')) or 'missing'}")
        print("---")


if __name__ == "__main__":
    main()
