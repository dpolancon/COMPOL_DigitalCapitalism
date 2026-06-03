# COMPOL Digital Capitalism: Pre-Flight Check & To-Do Report

**Date:** 2026-06-02
**Prompt ID:** PROMPT_05

## 1. Registry vs. Manifest Sync Report

- **Total PDFs in Manifest:** 63
- **Total Active Rows in Registry:** Could not verify (pandas not installed - requires prior installation check)
- **Path Mismatches Identified:**
  - **CRITICAL:** The `pdf_manifest.csv` contains **25 entries** with Windows-style paths:
    - Format: `"CHANDLER_FUCHS_eds\BOKENABMERKTE.pdf"` (backslashes)
    - Required format: `"CHANDLER_FUCHS_eds/BOKENABMERKTE.pdf"` (forward slashes)
    - These paths will fail on Linux/WSL
  - The manifest has these CHANDLER_FUCHS_eds files with backslash separators that need correction
- **Files Only in Manifest (not visible in current directory scan):**
  - BackMatter-2019.pdf
  - FrontMatter-2019.pdf
  - Index-2019.pdf
  - TableContents-2019.pdf
  - EditorsContributors-2019.pdf
- **Action Required:**
  1. Update `pdf_manifest.csv` to fix all 25 CHANDLER_FUCHS_eds paths (replace `\` with `/`)
  2. Verify existence of uploaded CHANDLER_FUCHS_eds PDFs (only 21 found, 25 expected)

## 2. Codebase Audit Findings

### `extract_hybryd.py` (Main Pipeline Entry Point)
**Status: PASS**
- ✓ Correct `argparse` setup
- ✓ Proper `logging.getLogger(__name__)` usage
- ✓ Loads Prompt_Bank from Excel `sheet_name='Prompt_Bank'`
- ✓ Filters by `RA_status == 'Not Started'`, `checkpoint_flag == 'GREEN'`, and excludes AUX_METADATA_OR_FRONTMATTER
- ✓ Fallback path resolution (`Path(args.pdf_dir) / filename`)
- ⚠ File name typo: `extract_hybryd.py` should be `extract_hybrid.py`

### `notebooklm_cli.py` (NotebookLM Wrapper)
**Status: PASS**
- ✓ Correct `logging.getLogger(__name__)` usage
- ✓ Proper subprocess handling for NotebookLM auth check
- ✓ JSON output parsing with error handling
- ✓ Temporary file cleanup with `missing_ok=True` for Python 3.11+

### `utils.py`
**Status: PASS**
- ✓ Correct `logging.getLogger(__name__)` usage
- ✓ Dynamic prompt loading from Excel
- ✓ YAML frontmatter generation for Obsidian notes
- ✓ Imports all required modules
- Note: Uses `needs_diego_review` (registry uses `needs_diegeo_review` - verify consistency)

### `api.py`
**Status: PASS**
- ✓ Correct `logging.getLogger(__name__)` usage
- ✓ PDF extraction with fallback (pdfplumber → PyPDF2)
- ✓ TogetherAI client with rate limit handling
- ✓ Environment variable loading

## 3. Environment Setup Commands (Copy-Paste Ready)

```bash
# 1. Navigate to repo root (WSL)
cd /mnt/c/ReposGitHub/COMPOL_DigitalCapitalism

# 2. Install/Upgrade dependencies
pip3 install --upgrade pandas openai pdfplumber PyPDF2 python-dotenv pyyaml openpyxl "notebooklm-py[browser]" playwright

# 3. Install Playwright browser (required for notebooklm-py)
playwright install chromium

# 4. Verify NotebookLM Auth (Must return valid JSON, not an error)
notebooklm auth check --test --json
```

## 4. Step-by-Step To-Do Checklist (Next Actions)

### Task 1: Fix Registry Section Header
- **Action:** Ensure Excel Registry section is named "Registry" (not incorrect fragment)
- **Why:** `pd.read_excel(..., sheet_name='Registry')` must match actual sheet name

### Task 2: Fix PDF Paths in pdf_manifest.csv
- **Action:** Update CSV to replace Windows backslashes with forward slashes
- **Command:**
```bash
cd /mnt/c/ReposGitHub/COMPOL_DigitalCapitalism
sed -i 's|\\CHANDLER_FUCHS_eds|/CHANDLER_FUCHS_eds|g' literature/pdf_manifest.csv
```
- **Why:** Linux/WSL paths must use forward slashes

### Task 3: Fix Excel relative_path for CHANDLER_FUCHS_eds files
- **Action:** Ensure `relative_path` in Excel includes `CHANDLER_FUCHS_eds/` prefix for all CHANDLER_FUCHS_eds PDFs
- **Files needing update (25 files):** BackMatter-2019.pdf through TableContents-2019.pdf
- **Why:** Subdirectory files must specify full relative path

### Task 4: Fix File Name Typo
- **Action:** Rename `extract_hybryd.py` → `extract_hybrid.py`
- **Why:** Biological spelling; consistency with PROJECT conventions

### Task 5: Verify Excel Data Consistency
- **Action:** Ensure all CHANDLER_FUCHS_eds files in Excel have:
  - `primary_cluster` = "AUX_METADATA_OR_FRONTMATTER" for FrontMatter, BackMatter, Index
  - `RA_status` = "Not Started"  
  - `priority` = "Low" (if excluded from primary cluster processing)

### Task 6: Ensure .env File Exists
- **Action:** Verify `/.env` contains `OPEN_API_KEY` and `OPEN_API_BASE`
- **Current:** Can be verified at `/.env`

### Task 7: Run Environment Setup Commands
- **Action:** Execute commands from Section 3 above
- **Why:** Dependencies must be installed before any pipeline execution

### Task 8: Execute Single-File Dry Run

```bash
cd /mnt/c/ReposGitHub/COMPOL_DigitalCapitalism
python3 -m src.notebooklm.extract_hybrid \
  --excel_path "/mnt/c/ReposGitHub/COMPOL_DigitalCapitalism/compol_digital_capitalism_vault/10_Literature/RA_NotebookLM_Obsidian_Registry.xlsx" \
  --pdf_dir "/mnt/c/ReposGitHub/COMPOL_DigitalCapitalism/literature/pdfs" \
  --output_dir "/mnt/c/ReposGitHub/COMPOL_DigitalCapitalism/compol_digital_capitalism_vault/10_Literature" \
  --source_id <SPECIFIC_ID> \
  --model "Qwen/Qwen3.5-9B"
```
- **Why:** Test end-to-end with single file before batch processing

### Task 9: Verify Output
- **Action:** Check generated `.md` file contains:
  - Correct YAML frontmatter with `type: source_note`
  - `source_id` matching input
  - Author year extracted from filename
  - Cluster information present
- **Why:** Validates prompt chain (P00 + PXX → P08 normalization)

### Task 10: Verify Excel Update
- **Action:** Confirm `RA_status` for processed source changes to `Saved in Obsidian`
- **Why:** Pipeline must update status to track progress

### Task 11: If Dry Run Succeeds, Run Full Batch
- **Action:** Remove `--source_id` argument from command
- **Why:** Process all eligible (`RA_status == 'Not Started'` + `checkpoint_flag == 'GREEN'`) sources

## 5. Context Gaps / Warnings

1. **Excel File Must Be Closed:** Windows Excel will cause "Permission Denied" errors when Python tries to save. Close before executing script.

2. **注意 `not_upload` folder:** The `CHANDLER_FUCHS_eds/not_upload/` directory exists—these files should NOT be processed or uploaded

3. **Elapsed Files to Exclude:** Ensure files marked with `EBSCO-Metadata` and raw metadata files have appropriate clusters (AUX_METADATA_OR_FRONTMATTER)

4. **Orchestrator Module Missing:** The referenced `orchestrator.py` doesn't exist. This may be an optional coordinator or legacy file.

5. **Seed File Status:** No CSV seed files visible—may be used for classifying documents into clusters where cluster assignments are missing.

6. **Backend CI Pending:** Backend startup and CI validation remain pending—runtime tests and integration checks required to confirm readiness.

---

**Summary:** Pipeline codebase is fundamentally sound with minor corrections needed. Primary blockers are Excel registry data consistency and Linux path migration for CHANDLER_FUCHS_eds files. Once fixed, dry-run testing validates before batch production.