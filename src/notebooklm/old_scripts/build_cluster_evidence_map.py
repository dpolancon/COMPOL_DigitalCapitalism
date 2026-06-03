#!/usr/bin/env python3
"""Build a cluster-to-Phase-1-note evidence map."""

import argparse
import json
import re
from pathlib import Path


def find_questions_dir() -> Path:
    for candidate in (Path("notes/questions"), Path("03_notes/questions")):
        if candidate.exists():
            return candidate
    raise FileNotFoundError("Could not find Phase 1 notes in notes/questions or 03_notes/questions")


def section(text: str, heading: str, next_heading: str | None = None) -> str:
    if next_heading:
        pattern = rf"{re.escape(heading)}\s*(.*?)(?=\n{re.escape(next_heading)})"
    else:
        pattern = rf"{re.escape(heading)}\s*(.*)"
    match = re.search(pattern, text, re.S)
    return match.group(1).strip() if match else ""


def frontmatter_value(text: str, key: str) -> str:
    match = re.search(rf'^{re.escape(key)}:\s*"?([^"\n]+)"?', text, re.M)
    return match.group(1).strip() if match else ""


def main() -> None:
    parser = argparse.ArgumentParser(description="Build cluster evidence map from Phase 1 notes.")
    parser.add_argument("--registry", default="02_LitRev_Sistematica/config/registry_parsed.json")
    parser.add_argument("--output", default="02_LitRev_Sistematica/derived/cluster_evidence_map.json")
    args = parser.parse_args()

    registry = json.loads(Path(args.registry).read_text(encoding="utf-8"))
    questions_dir = find_questions_dir()
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    papers_by_id = {p["source_id"]: p for p in registry.get("papers", [])}
    result: dict[str, dict] = {}
    for cluster in registry.get("clusters", []):
        cid = cluster["cluster_id"]
        notes = []
        source_ids = cluster.get("paper_ids", [])
        related_questions = [q for q in registry["questions"] if q["source_id"] in source_ids]
        related_questions.sort(key=lambda q: q["question_id"])
        for q in related_questions:
            path = questions_dir / f"{q['question_id']}.md"
            text = path.read_text(encoding="utf-8") if path.exists() else ""
            notes.append(
                {
                    "note_id": q["question_id"],
                    "source_id": q["source_id"],
                    "paper_title": q["paper_title"],
                    "note_path": str(path),
                    "question_text": q["question_text"],
                    "status": frontmatter_value(text, "status") if text else "missing",
                    "distilled_note": section(text, "## Distilled note", "## Evidence / page anchors") if text else "",
                    "evidence_page_anchors": section(text, "## Evidence / page anchors", "## Links") if text else "",
                }
            )

        result[cid] = {
            "cluster_id": cid,
            "cluster_name": cluster.get("cluster_name", ""),
            "source_ids": source_ids,
            "source_titles": [papers_by_id[s]["title"] for s in source_ids if s in papers_by_id],
            "per_paper_note_ids": [n["note_id"] for n in notes],
            "notes": notes,
        }

    output_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {output_path} with {len(result)} clusters from {questions_dir}")


if __name__ == "__main__":
    main()
