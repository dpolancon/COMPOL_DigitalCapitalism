#!/usr/bin/env python3
"""Convert notes accidentally saved as JSON strings back to markdown."""

import argparse
import json
from pathlib import Path


def repair(path: Path, dry_run: bool) -> bool:
    text = path.read_text(encoding="utf-8")
    if not text.startswith('"---\\n'):
        return False

    try:
        decoded = json.loads(text)
    except json.JSONDecodeError:
        if text.startswith('"') and text.endswith('"'):
            text = text[1:-1]
        decoded = text.replace("\\n", "\n").replace('\\"', '"')

    if dry_run:
        print(f"Would repair {path}")
    else:
        path.write_text(decoded, encoding="utf-8")
        print(f"Repaired {path}")
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description="Repair escaped markdown note files.")
    parser.add_argument("--dir", type=Path, default=Path("notes/questions"))
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    count = 0
    for path in sorted(args.dir.glob("PDF*_Q*.md")):
        if repair(path, args.dry_run):
            count += 1
    print(f"{'Would repair' if args.dry_run else 'Repaired'} {count} file(s).")


if __name__ == "__main__":
    main()
