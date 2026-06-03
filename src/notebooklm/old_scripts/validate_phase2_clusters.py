#!/usr/bin/env python3
"""Validate Phase 2 cluster synthesis notes."""

import argparse
import json
import re
from collections import Counter
from datetime import date
from pathlib import Path

REQUIRED_SECTIONS = [
    "## Cluster scope",
    "## NotebookLM answer",
    "## Cross-paper evidence map",
    "## Synthesis note",
    "## Tensions, limits, and open questions",
    "## Links to related notes",
    "## Memo relevance",
]


def load_json(path: str | Path) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def questions_dir() -> Path:
    for candidate in (Path("notes/questions"), Path("03_notes/questions")):
        if candidate.exists():
            return candidate
    return Path("notes/questions")


def parse_frontmatter(text: str) -> dict | None:
    match = re.match(r"^---\s*\n(.*?)\n---", text, re.S)
    if not match:
        return None
    result = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = value.strip()
        try:
            result[key.strip()] = json.loads(value)
        except json.JSONDecodeError:
            result[key.strip()] = value.strip('"')
    return result


def section_content(text: str, heading: str) -> str:
    match = re.search(rf"{re.escape(heading)}\s*(.*?)(?=\n## |\Z)", text, re.S)
    return match.group(1).strip() if match else ""


def validate(registry: dict, output_dir: Path) -> tuple[list[str], dict]:
    questions = registry.get("cluster_questions", [])
    errors: list[str] = []
    qids = [q["cluster_question_id"] for q in questions]
    for qid, count in Counter(qids).items():
        if count > 1:
            errors.append(f"Duplicate cluster question ID in registry: {qid}")

    qdir = questions_dir()
    counts = Counter()
    for q in questions:
        qid = q["cluster_question_id"]
        path = output_dir / f"{qid}.md"
        counts[q["cluster_id"]] += 1
        if not path.exists():
            errors.append(f"Missing cluster note: {path}")
            continue

        text = path.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        if fm is None:
            errors.append(f"Malformed YAML frontmatter: {path}")
            continue

        if fm.get("status") != "draft":
            errors.append(f"{qid}: status is not draft")
        if fm.get("cluster_id") != q["cluster_id"]:
            errors.append(f"{qid}: cluster_id mismatch ({fm.get('cluster_id')} != {q['cluster_id']})")
        if fm.get("question_id") != q["question_id"]:
            errors.append(f"{qid}: question_id mismatch")
        if fm.get("cluster_question_id") != qid:
            errors.append(f"{qid}: cluster_question_id mismatch")
        if "[NOTEBOOKLM_CLUSTER]" not in text:
            errors.append(f"{qid}: missing [NOTEBOOKLM_CLUSTER]")
        if "[DRAFT_BY_QWEN]" in text:
            errors.append(f"{qid}: contains [DRAFT_BY_QWEN]")
        if "Paste the NotebookLM answer" in text or "[Paste" in text:
            errors.append(f"{qid}: contains placeholder answer field")

        answer = section_content(text, "## NotebookLM answer")
        if not answer or answer.strip() == "[NOTEBOOKLM_CLUSTER]":
            errors.append(f"{qid}: empty NotebookLM answer")

        for section in REQUIRED_SECTIONS:
            if section not in text:
                errors.append(f"{qid}: missing section {section}")

        related = fm.get("related_per_paper_notes", [])
        if not isinstance(related, list) or not related:
            errors.append(f"{qid}: missing related_per_paper_notes list")
        for note_id in related if isinstance(related, list) else []:
            if not (qdir / f"{note_id}.md").exists():
                errors.append(f"{qid}: related note does not exist: {note_id}")

    summary = {
        "cluster_questions": len(questions),
        "notes_expected": len(questions),
        "notes_found": len(list(output_dir.glob("C*_Q*.md"))) if output_dir.exists() else 0,
        "errors": len(errors),
        "counts_by_cluster": dict(sorted(counts.items())),
        "phase1_questions_dir": str(qdir),
    }
    return errors, summary


def write_report(errors: list[str], summary: dict, report_path: Path) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)
    status = "PASS" if not errors else "FAIL"
    lines = [
        "# Phase 2 Cluster Validation Report",
        "",
        f"Date: {date.today().isoformat()}",
        f"Status: {status}",
        "",
        "## Summary",
        "",
        f"- Cluster questions expected: {summary['cluster_questions']}",
        f"- Cluster notes found: {summary['notes_found']}",
        f"- Errors: {summary['errors']}",
        f"- Phase 1 notes directory used: `{summary['phase1_questions_dir']}`",
        "",
        "## Counts By Cluster",
        "",
    ]
    for cid, count in summary["counts_by_cluster"].items():
        lines.append(f"- {cid}: {count}")
    lines.extend(["", "## Errors", ""])
    if errors:
        lines.extend(f"- {e}" for e in errors)
    else:
        lines.append("- None")
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate generated Phase 2 cluster notes.")
    parser.add_argument("--registry", default="02_LitRev_Sistematica/config/registry_parsed.json")
    parser.add_argument("--output-dir", default="notes/clusters")
    parser.add_argument("--report", default="02_LitRev_Sistematica/reports/phase2_cluster_validation_report.md")
    args = parser.parse_args()

    errors, summary = validate(load_json(args.registry), Path(args.output_dir))
    write_report(errors, summary, Path(args.report))
    print(f"Phase 2 validation: {'PASS' if not errors else 'FAIL'}")
    print(f"Expected: {summary['notes_expected']} | Found: {summary['notes_found']} | Errors: {summary['errors']}")
    print(f"Report: {args.report}")
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
