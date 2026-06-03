"""Validate Phase 3A synthesis artifacts.

The validator is conservative: it checks file presence, extraction schema,
claim integrity, memo architecture, and obvious credential patterns without
printing any secret values.
"""

from __future__ import annotations

import csv
import re
import subprocess
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "04_review_artifacts"
REPORT = OUT / "05_reports/phase3a_validation_report.md"

REQUIRED_FILES = [
    ROOT / "05_skills/SKILL_PHASE3_LANDRENT_SYNTHESIS.md",
    OUT / "00_protocol/phase3_synthesis_protocol.md",
    OUT / "01_registries/source_registry.csv",
    OUT / "01_registries/question_registry.csv",
    OUT / "01_registries/cluster_question_registry.csv",
    OUT / "01_registries/note_integrity_report.md",
    OUT / "02_extraction/extraction_matrix.csv",
    OUT / "02_extraction/concept_dictionary.md",
    OUT / "02_extraction/mechanism_ledger.md",
    OUT / "02_extraction/variable_parameter_ledger.md",
    OUT / "03_synthesis/thematic_synthesis_map.md",
    OUT / "03_synthesis/claim_cluster_table.csv",
    OUT / "03_synthesis/gap_and_transportability_memo.md",
    OUT / "04_memo_architecture/detailed_memo_outline.md",
    OUT / "04_memo_architecture/paragraph_function_map.csv",
]

REQUIRED_SCHEMA = [
    "claim_id",
    "source_id",
    "question_id",
    "paper_key",
    "page_ref",
    "dimension",
    "concept",
    "definition",
    "mechanism",
    "causal_chain",
    "variables_parameters",
    "theory_evidence_status",
    "claim_text",
    "project_use",
    "validation_status",
    "reviewer_comment",
]

MANDATORY_CONCEPTS = [
    "land",
    "land rent",
    "housing rent",
    "real estate",
    "productive capital",
    "wealth",
    "land price",
    "fundamental value",
    "bubble",
    "land overvaluation",
    "collateral value",
    "leverage",
    "unbalanced growth",
    "R versus G",
    "debt rollover",
]

MANDATORY_MECHANISMS = [
    "land speculation crowds out productive capital",
    "real-estate credit amplifies land-price inflation",
    "leverage creates land-bubble phase transition",
    "unbalanced growth separates land prices from rents",
    "land changes R versus G and debt-rollover conditions",
    "land taxation/regulation redirects savings toward productive investment",
    "land/wealth measurement distinction affects interpretation of capital accumulation",
    "wobbly dynamics produces endogenous instability and bounded boom-bust paths",
]

THEMES = [
    "Definitions and conceptual separations",
    "Asset-price and wealth-measurement claims",
    "Growth and capital-formation mechanisms",
    "Credit, leverage, collateral, and monetary policy",
    "Unbalanced growth and overvaluation",
    "Debt rollover and dynamic efficiency",
    "Wobbly dynamics and endogenous instability",
    "Policy and institutional implications",
    "Critical adaptation to urban land-rent financialization in Latin America",
]

MEMO_SECTIONS = [
    "Introduction: why this literature matters for land rent and financialization",
    "Method: corpus, notes, extraction protocol, screening, synthesis",
    "Conceptual objects: land, rent, wealth, capital, real estate, bubble",
    "Mechanism I: land-price inflation and capital-formation crowding-out",
    "Mechanism II: credit expansion, collateral, leverage, and monetary policy",
    "Mechanism III: unbalanced growth and the Land Overvaluation Theorem",
    "Mechanism IV: R versus G, land, and infinite debt rollover",
    "Wobbly dynamics and instability as supplementary branch",
    "Critical appraisal: assumptions, scope, Latin American transportability",
    "Research agenda: what the Fondecyt project should retain, modify, or reject",
    "Conclusion",
]

PARAGRAPH_COLUMNS = [
    "paragraph_id",
    "section",
    "paragraph_function",
    "core_claim",
    "source_ids",
    "note_ids",
    "claim_ids",
    "concepts",
    "mechanisms",
    "variables_parameters",
    "validation_status",
    "draft_ready",
    "reviewer_comment",
]

ALLOWED_DRAFT_STATUSES = {"validated_exact", "validated_paraphrase", "needs_page"}
SECRET_PATTERNS = [
    ("OpenAI-style key", re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b")),
    ("Together-style key", re.compile(r"\btgp_v1_[A-Za-z0-9_-]{20,}\b")),
    ("Google API key", re.compile(r"\bAIza[0-9A-Za-z_-]{20,}\b")),
    ("GitHub token", re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b")),
]


def rel(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def tracked_files() -> list[Path]:
    try:
        result = subprocess.run(
            ["git", "ls-files"],
            cwd=ROOT,
            check=True,
            text=True,
            capture_output=True,
        )
    except Exception:
        return []
    paths = []
    for line in result.stdout.splitlines():
        path = ROOT / line
        if path.exists() and path.is_file():
            paths.append(path)
    return paths


def text_file(path: Path) -> bool:
    if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".pdf", ".xlsx", ".zip", ".docx"}:
        return False
    try:
        path.read_text(encoding="utf-8")
        return True
    except Exception:
        return False


def scan_secrets() -> list[str]:
    findings = []
    scan_paths = set(tracked_files())
    scan_paths.update((ROOT / ".continue").rglob("*"))
    scan_paths.update((ROOT / "05_skills").rglob("*"))
    scan_paths.update((ROOT / "scripts").rglob("*.py"))
    for path in sorted(scan_paths):
        if not path.is_file() or not text_file(path):
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for label, pattern in SECRET_PATTERNS:
            if pattern.search(text):
                findings.append(f"{label} pattern found in `{rel(path)}`. Value suppressed; rotate if this is a real credential.")
                break
    return findings


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    for path in REQUIRED_FILES:
        if not path.exists():
            errors.append(f"Missing required file: `{rel(path)}`")
    if not list((OUT / "05_reports").glob("phase3a_execution_report_*.md")):
        errors.append("Missing required file: `04_review_artifacts/05_reports/phase3a_execution_report_YYYY-MM-DD.md`")

    claims: list[dict[str, str]] = []
    extraction = OUT / "02_extraction/extraction_matrix.csv"
    if extraction.exists():
        with extraction.open("r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            fieldnames = reader.fieldnames or []
            for col in REQUIRED_SCHEMA:
                if col not in fieldnames:
                    errors.append(f"Missing extraction schema column: `{col}`")
            claims = list(reader)
        claim_ids = [row.get("claim_id", "") for row in claims]
        duplicates = [cid for cid, count in Counter(claim_ids).items() if cid and count > 1]
        if duplicates:
            errors.append(f"Duplicate claim IDs: {', '.join(duplicates[:20])}")
        for row in claims:
            if not row.get("dimension"):
                errors.append(f"Claim `{row.get('claim_id', '<missing>')}` lacks dimension")
            if not row.get("claim_text"):
                errors.append(f"Claim `{row.get('claim_id', '<missing>')}` lacks claim_text")
    else:
        errors.append("Cannot validate extraction matrix because it is missing.")

    concept_text = (OUT / "02_extraction/concept_dictionary.md").read_text(encoding="utf-8") if (OUT / "02_extraction/concept_dictionary.md").exists() else ""
    for concept in MANDATORY_CONCEPTS:
        if f"## {concept}" not in concept_text:
            errors.append(f"Mandatory concept missing: `{concept}`")

    mechanism_text = (OUT / "02_extraction/mechanism_ledger.md").read_text(encoding="utf-8") if (OUT / "02_extraction/mechanism_ledger.md").exists() else ""
    for mechanism in MANDATORY_MECHANISMS:
        if f"## {mechanism}" not in mechanism_text:
            errors.append(f"Mandatory mechanism missing: `{mechanism}`")

    theme_text = (OUT / "03_synthesis/thematic_synthesis_map.md").read_text(encoding="utf-8") if (OUT / "03_synthesis/thematic_synthesis_map.md").exists() else ""
    for theme in THEMES:
        if theme not in theme_text:
            errors.append(f"Required synthesis cluster missing: `{theme}`")

    outline_text = (OUT / "04_memo_architecture/detailed_memo_outline.md").read_text(encoding="utf-8") if (OUT / "04_memo_architecture/detailed_memo_outline.md").exists() else ""
    for section in MEMO_SECTIONS:
        if section not in outline_text:
            errors.append(f"Required memo outline section missing: `{section}`")

    paragraph_map = OUT / "04_memo_architecture/paragraph_function_map.csv"
    paragraph_rows: list[dict[str, str]] = []
    if paragraph_map.exists():
        with paragraph_map.open("r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            fieldnames = reader.fieldnames or []
            for col in PARAGRAPH_COLUMNS:
                if col not in fieldnames:
                    errors.append(f"Missing paragraph map column: `{col}`")
            paragraph_rows = list(reader)
        claim_status = {row.get("claim_id", ""): row.get("validation_status", "") for row in claims}
        not_supported = {row.get("claim_id", "") for row in claims if row.get("validation_status") == "not_supported"}
        for row in paragraph_rows:
            ids = [cid.strip() for cid in row.get("claim_ids", "").split(";") if cid.strip()]
            if row.get("draft_ready", "").lower() == "true":
                for cid in ids:
                    status = claim_status.get(cid, "")
                    if status not in ALLOWED_DRAFT_STATUSES:
                        errors.append(f"Paragraph `{row.get('paragraph_id')}` is draft_ready but uses `{cid}` with status `{status}`")
                if "needs_page" in row.get("validation_status", "") and not row.get("reviewer_comment"):
                    errors.append(f"Paragraph `{row.get('paragraph_id')}` uses needs_page claims without reviewer_comment")
            bad = [cid for cid in ids if cid in not_supported]
            if bad:
                errors.append(f"Paragraph `{row.get('paragraph_id')}` uses not_supported claims: {', '.join(bad)}")
    else:
        errors.append("paragraph_function_map.csv is missing.")

    secret_findings = scan_secrets()
    if secret_findings:
        warnings.extend(secret_findings)

    status = "PASS" if not errors else "FAIL"
    report = [
        "# Phase 3A Validation Report",
        "",
        f"Status: {status}",
        "",
        "## Summary",
        "",
        f"- Required files checked: {len(REQUIRED_FILES)}",
        f"- Claims checked: {len(claims)}",
        f"- Paragraph rows checked: {len(paragraph_rows)}",
        f"- Errors: {len(errors)}",
        f"- Warnings: {len(warnings)}",
        "",
        "## Errors",
        "",
        "\n".join(f"- {item}" for item in errors) if errors else "- None",
        "",
        "## Warnings",
        "",
        "\n".join(f"- {item}" for item in warnings) if warnings else "- None",
        "",
        "## Notes",
        "",
        "- Secret-pattern warnings suppress the actual value. Rotate credentials if the finding is real.",
        "- `needs_page` claims are allowed in Phase 3A artifacts but should be verified before final memo drafting.",
    ]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(report).rstrip() + "\n", encoding="utf-8")
    update_execution_report(status, len(errors), len(warnings))
    print(f"Phase 3A validation: {status}")
    print(f"Claims: {len(claims)}")
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")
    print(f"Report: {rel(REPORT)}")
    return 0 if not errors else 1


def update_execution_report(status: str, error_count: int, warning_count: int) -> None:
    reports = sorted((OUT / "05_reports").glob("phase3a_execution_report_*.md"))
    if not reports:
        return
    path = reports[-1]
    text = path.read_text(encoding="utf-8")
    replacement = (
        f"Phase 3A validation status: {status}. "
        f"Errors: {error_count}. Warnings: {warning_count}. "
        "`04_review_artifacts/05_reports/phase3a_validation_report.md` contains the full report."
    )
    text = re.sub(
        r"## Validation Result\n\n.*?\n\n## Unresolved Issues",
        f"## Validation Result\n\n{replacement}\n\n## Unresolved Issues",
        text,
        flags=re.DOTALL,
    )
    path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
