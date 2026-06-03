---
prompt_id: PROMPT_05
title: Pre-Flight Check & To-Do Generation for NotebookLM Automation
date: 2026-06-02
target_output: 81_Outputs/2026-06-02_PreFlight_Check.md
status: ACTIVE
---

# ROLE & OBJECTIVE
You are the Lead DevOps and Research Architect for the COMPOL_DigitalCapitalism project. Your objective is to conduct a rigorous pre-flight audit of the automated NotebookLM + Together.ai literature extraction pipeline. You will cross-reference the updated registry and manifest, audit the Python codebase, and generate a precise, executable "To-Do" checklist to guarantee 100% readiness for the first automated batch run via the `qwen` terminal.

# CONTEXT & INPUTS
- **Registry:** `RA_NotebookLM_Obsidian_Registry.xlsx` (Recently updated to exclude metadata/front-matter files).
- **Manifest:** `literature/pdf_manifest.csv` (Recently updated with current PDF paths and sizes).
- **Codebase:** `src/notebooklm/` (Contains `extract_hybrid.py`, `notebooklm_cli.py`, `utils.py`, `api.py`, `__init__.py`).
- **Environment:** Linux/WSL terminal (paths use `/mnt/c/...` or relative paths from repo root).

# INSTRUCTIONS FOR ANALYSIS

## 1. Registry vs. Manifest Synchronization
- Cross-reference the `source_id`, `filename`, and `relative_path` columns in the Excel Registry against the `pdf_manifest.csv`.
- Identify any PDFs present in the manifest but missing from the registry, or vice versa.
- Flag any `relative_path` mismatches that would cause a `FileNotFoundError` in a Linux/WSL environment (e.g., Windows backslashes `\` instead of forward slashes `/`, or missing `CHANDLER_FUCHS_eds/` subfolder prefixes).

## 2. Python Codebase Audit
- Review the logic in `extract_hybrid.py`, `notebooklm_cli.py`, `utils.py`, and `api.py`.
- Check for:
  - Correct dynamic loading of the `Prompt_Bank` sheet from the Excel file.
  - Proper handling of the `P08_CHATGPT_NORMALIZE_TO_OBSIDIAN` prompt.
  - Robust path resolution (using `pathlib.Path` correctly for cross-platform compatibility).
  - Correct `argparse` setup and Excel sheet name targeting (`sheet_name='Registry'`).
  - Any missing imports or syntax errors (e.g., `logging.getLogger(__name__)` instead of `name`).

## 3. Environment & Dependency Verification
- List the exact terminal commands required to:
  1. Navigate to the correct repository root in WSL.
  2. Verify/install all required Python packages (`pandas`, `openai`, `pdfplumber`, `PyPDF2`, `python-dotenv`, `pyyaml`, `openpyxl`, `notebooklm-py[browser]`).
  3. Verify Playwright browser installation (`playwright install chromium`).
  4. Test NotebookLM authentication (`notebooklm auth check --test --json`).

## 4. Dry-Run Protocol Definition
- Define the exact, copy-pasteable terminal command to execute a **single-file dry run** (e.g., targeting `--source_id PDF_059` or `PDF_003`) to validate the end-to-end pipeline (NotebookLM extraction → Together.ai normalization → Obsidian save → Excel status update) before running the full batch.

# REQUIRED OUTPUT FORMAT
Output a single, comprehensive Markdown report. Do not use conversational filler. Use the following exact structure, ready to be saved to `81_Outputs/2026-06-02_PreFlight_Check.md`:

# COMPOL Digital Capitalism: Pre-Flight Check & To-Do Report
**Date:** 2026-06-02
**Prompt ID:** PROMPT_05

## 1. Registry vs. Manifest Sync Report
- **Total PDFs in Manifest:** [Count]
- **Total Active Rows in Registry:** [Count]
- **Path/Name Mismatches:** [List any specific files where `relative_path` in Excel does not match `relative_path` in CSV, or note "None - Perfect Sync"]
- **Action Required:** [e.g., "Update Excel relative_path for PDF_051 to include 'CHANDLER_FUCHS_eds/'"]

## 2. Codebase Audit Findings
- **`extract_hybrid.py`:** [Status: Pass/Fail + specific fix if needed]
- **`notebooklm_cli.py`:** [Status: Pass/Fail + specific fix if needed]
- **`utils.py`:** [Status: Pass/Fail + specific fix if needed]
- **`api.py`:** [Status: Pass/Fail + specific fix if needed]

## 3. Environment Setup Commands (Copy-Paste Ready)
```bash
# 1. Navigate to repo root (WSL)
cd /mnt/c/ReposGitHub/COMPOL_DigitalCapitalism

# 2. Install/Upgrade dependencies
pip3 install --upgrade pandas openai pdfplumber PyPDF2 python-dotenv pyyaml openpyxl "notebooklm-py[browser]"

# 3. Install Playwright browser
playwright install chromium

# 4. Verify NotebookLM Auth (Must return valid JSON, not an error)
notebooklm auth check --test --json
```

## 4. Step-by-Step To-Do Checklist (Next Actions)

- **Task 1:** [Specific action, e.g., "Fix the `relative_path` for PDF_051 in the Excel Registry"]
- **Task 2:** [Specific action, e.g., "Ensure `.env` file exists in repo root with `OPEN_API_KEY`"]
- **Task 3:** [Specific action, e.g., "Run the Environment Setup Commands above"]
- **Task 4:** **Execute Single-File Dry Run:**
    
```bash
	python3 -m src.notebooklm.extract_hybrid \
	--excel_path "/mnt/c/ReposGitHub/COMPOL_DigitalCapitalism/compol_digital_capitalism_vault/10_Literature/RA_NotebookLM_Obsidian_Registry.xlsx" \
	  --pdf_dir "/mnt/c/ReposGitHub/COMPOL_DigitalCapitalism/literature/pdfs" \
	  --output_dir "/mnt/c/ReposGitHub/COMPOL_DigitalCapitalism/compol_digital_capitalism_vault/10_Literature" \
	  --source_id PDF_059 \
	  --model "Qwen/Qwen3.5-9B"
```

- **Task 5:** Verify the output `.md` file in Obsidian has correct YAML frontmatter and content.
- **Task 6:** Verify the Excel Registry `RA_status` for `PDF_059` changed to `Saved in Obsidian`.
- **Task 7:** If dry run succeeds, remove `--source_id PDF_059` from the command above to unleash the full batch.

## 5. Context Gaps / Warnings

[List any assumptions made or potential edge cases, e.g., "Ensure the Excel file is closed in Windows before running the Python script to prevent 'Permission Denied' errors."]


***
