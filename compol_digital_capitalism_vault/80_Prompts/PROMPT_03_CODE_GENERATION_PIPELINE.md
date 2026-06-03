---
prompt_id: PROMPT_03
title: Code Generation - NotebookLM Automation Pipeline
date: 2026-06-02
target_output: C:/ReposGitHub/COMPOL_DigitalCapitalism/compol_digital_capitalism_vault/81_Outputs/2026-06-02_Pass03_Code_Generation.md
status: ACTIVE
---

# ROLE & OBJECTIVE
You are the Lead Python Developer for the COMPOL_DigitalCapitalism project. Your objective is to refactor legacy automation scripts into a modern, modular Python pipeline that reads an Excel registry, queries the Together.ai API (via Qwen models), and generates strictly formatted Obsidian literature notes.

# CONTEXT & DATA SCHEMAS

## 1. Excel Registry Columns (from RA_NotebookLM_Obsidian_Registry.xlsx)
The script must read an Excel file with the following exact columns:
- `source_id` (e.g., PDF_001)
- `filename` (e.g., ALVAREZ-FUENTES_ETAL_2024.pdf)
- `relative_path`
- `primary_cluster` (e.g., G4_CHILE_LATAM_CASE_CONTEXT)
- `secondary_cluster`
- `priority` (High, Medium, Low, Review)
- `checkpoint_flag` (GREEN, YELLOW, RED)
- `RA_status` (Not Started, Saved in Obsidian, Needs Rework)
- `prompt_ids_to_run` (e.g., "P00_UNIVERSAL_SOURCE_EXTRACTION + P04_CHILE_LATAM_CONTEXT")
- `output_obsidian_note` (e.g., PDF_001_ALVAREZ-FUENTES_ETAL_2024.md)

## 2. Required Obsidian YAML Frontmatter Schema
Every generated Markdown note MUST start with this exact YAML block:
```yaml
---
type: source_note
status: draft_ra
source_id: [INSERT source_id]
filename: [INSERT filename]
author_year: [EXTRACT FROM TEXT OR FILENAME]
clusters: [INSERT primary_cluster, secondary_cluster]
priority: [INSERT priority]
needs_diegeo_review: yes
---
```

# INSTRUCTIONS

## 1. Analyze Legacy Code

Review the legacy scripts provided in the attached `@src/notebooklm/old_scripts` directory. Identify reusable logic for API handling, batching, and error management.

## 2. Generate Modular Python Architecture

Write the complete, production-ready Python code for the following file structure. Use `pandas` for Excel handling, `PyPDF2` or `pymupdf` for PDF text extraction, and the `openai` Python client for the Together.ai API.

### File 1: `src/notebooklm/api.py`

- Create a wrapper class `TogetherAIClient`.
- Initialize with `base_url="https://api.together.ai/v1"` and `api_key` (loaded from `.env`).
- Method `extract_text(pdf_path, max_pages=5)`: Extracts the first 5 pages of a PDF.
- Method `query_llm(prompt_text, model="Qwen/Qwen3.5-9B")`: Sends the prompt to Together.ai and returns the raw markdown response. Include exponential backoff retry logic for rate limits.

### File 2: `src/notebooklm/extract_literature.py`

- This is the main CLI entry point.
- Arguments: `--excel_path`, `--pdf_dir`, `--output_dir`, `--model` (default: "Qwen/Qwen3.5-9B").
- Logic:
    1. Load the Excel registry using pandas.
    2. Filter rows where `RA_status == 'Not Started'` and `priority == 'High'` (or allow filtering by `source_id`).
    3. For each row: a. Construct the system prompt based on the `prompt_ids_to_run` column (map these to the actual prompt text from the registry). b. Extract text from the PDF using `api.py`. c. Combine the system prompt and the PDF text. d. Call the LLM via `api.py`. e. Parse the LLM output to ensure it contains the required YAML frontmatter. f. Save the output as a `.md` file in the `--output_dir` using the `output_obsidian_note` filename. g. Update the Excel registry row `RA_status` to 'Processed_Pending_Review'.

### File 3: `src/notebooklm/utils.py`

- Helper functions for loading environment variables, validating YAML frontmatter, and mapping `prompt_ids_to_run` strings to actual prompt templates.

- Include a PROMPT_REGISTRY dictionary mapping the exact prompt IDs (e.g., "P00_UNIVERSAL_SOURCE_EXTRACTION") to their actual prompt text, OR write a function to load them dynamically from a local prompts/ directory.


# REQUIRED OUTPUT FORMAT

Output a single, comprehensive Markdown report containing the complete, copy-pasteable Python code for each file.

- Use standard Python typing and docstrings.
- Do not use conversational filler.
- Format the output so it can be directly saved to `C:/ReposGitHub/COMPOL_DigitalCapitalism/compol_digital_capitalism_vault/81_Outputs/2026-06-02_Pass03_Code_Generation.md`.


