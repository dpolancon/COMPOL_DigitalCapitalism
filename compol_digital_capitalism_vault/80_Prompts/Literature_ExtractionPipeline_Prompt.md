# MISSION: Execute COMPOL Digital Capitalism Literature Extraction Pipeline

You are an autonomous execution agent tasked with running the literature extraction pipeline for the `COMPOL_DigitalCapitalism` repository. Your goal is to process the literature registry using the `extract_hybrid.py` pipeline (NotebookLM extraction + Qwen normalization) to generate one structured `.md` Obsidian note per PDF source. 

## ⚠️ CRITICAL CONSTRAINTS
1. EXCLUSION: You MUST explicitly skip `PDF_012` (`DIGITAL_COMPASS_REPORT.pdf`), as it is an AUX_METADATA_OR_FRONTMATTER file, not a source.
2. OUTPUT: All generated notes must be saved as individual `.md` files in `compol_digital_capitalism_vault\10_Literature\`.
3. INTEGRATION: Do NOT attempt to merge, cluster, or synthesize the notes. Your only job is 1-to-1 extraction and normalization per paper.
4. SAFETY: Do not alter the core logic of `extract_hybrid.py` unless patching the known `OPEN_API_BASE` environment variable bug.

## 🛠️ PHASE 1: PRE-FLIGHT CHECKS & ENVIRONMENT SETUP
Before running any extraction, execute and verify the following steps. If any step fails, halt and report the error.
1. Install dependencies:
	```bash
   pip install -r requirements.txt
   pip install pyyaml openpyxl "notebooklm-py[browser]"
   playwright install chromium
	```

2. Verify `.env` file: Ensure `OPEN_API_BASE=https://api.together.ai/v1` is present alongside `OPEN_API_KEY`. If missing, append it.
3. Authenticate with NotebookLM:

   
```bash
    notebooklm login
	notebooklm auth check --test --json
```

2. _(Confirm the output returns `{"status": "ok"}`)_

## 🚀 PHASE 2: EXECUTION STRATEGY

Run the hybrid extraction pipeline. To ensure stability and avoid rate limits, process the "GREEN" priority sources in logical cluster batches, explicitly excluding `PDF_012`.

Use the following base command structure, adjusting the `--source_id` for batch processing or individual runs:

   
```bash
python -m src.notebooklm.extract_hybrid \
  --excel_path "compol_digital_capitalism_vault\10_Literature\RA_NotebookLM_Obsidian_Registry.xlsx" \
  --pdf_dir "literature" \
  --output_dir "compol_digital_capitalism_vault\10_Literature" \
  --model "Qwen/Qwen3.5-9B"
```


**Recommended Batch Execution Order:**

- **Batch 1 (Dry Run):** `--source_id PDF_059` (Fuchs-Introduction-2019.pdf, ~1MB, verifies the whole pipeline works).
- **Batch 2 (G6 Digital Capitalism):** PDF_051, PDF_052, PDF_057, PDF_058, PDF_059, PDF_060, PDF_061, PDF_068
- **Batch 3 (G4 Chile/LatAm):** PDF_003, PDF_005, PDF_011, PDF_022, PDF_027, PDF_034, PDF_037
- **Batch 4 (G2 Topic Modeling):** PDF_024, PDF_035, PDF_044, PDF_045, PDF_066
- **Batch 5 (G3 Platformization):** PDF_033, PDF_040
- **Batch 6 (G1 Paid Ads):** PDF_006, PDF_026, PDF_043
- **Batch 7 (G5 Ethics):** PDF_013

_(Note: If the script supports running all GREEN sources at once via a flag, you may do so, but you MUST ensure `PDF_012` is filtered out by checking that `primary_cluster != "AUX_METADATA_OR_FRONTMATTER"`)._

## ✅ PHASE 3: VERIFICATION & REPORTING

After execution, perform the following checks and report back to me:

1. Confirm that `.md` files were successfully created in `compol_digital_capitalism_vault\10_Literature\` for the processed source IDs.
2. Open one generated `.md` file (e.g., `PDF_059_Fuchs-Introduction-2019.md`) and verify it contains:
    - Valid YAML frontmatter.
    - Proper Markdown section headers (as defined by Prompt P08).
3. Confirm that the `RA_NotebookLM_Obsidian_Registry.xlsx` was updated (e.g., `RA_status` changed to "Saved in Obsidian" or "Processed_Pending_Review" for the processed rows).
4. Report any errors, timeouts, or skipped files (especially confirming `PDF_012` was safely ignored).

Begin with Phase 1 now.


