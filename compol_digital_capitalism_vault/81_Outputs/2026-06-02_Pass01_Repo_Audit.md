# COMPOL Digital Capitalism: First Pass Audit Report
**Date:** 2026-06-02
**Prompt ID:** PROMPT_01

## 1. Executive Summary
The repository is well-structured with clear separation between source code, literature vault, and output directories. Core scripts reside under `src/notebooklm/` and legacy automation scripts are present in `src/notebooklm/old_scripts`. Minor issues include inconsistent YAML frontmatter in vault notes and missing validation rules for new literature entries. Overall health is good, but immediate action is needed to modernize legacy scripts and enforce strict YAML schema.

## 2. Legacy Script Curation (`src/notebooklm/`)
- **Extracted Logic:** The `old_scripts` directory contains reusable components for NotebookLM API handling, batch processing, and error management. Functions such as `api_request()`, `batch_process_notes()`, and `retry_wrapper()` are identified as valuable.
- **Proposed Architecture:** Create a modular package `notebooklm` with submodules:
  - `api.py` – encapsulates all NotebookLM API interactions.
  - `batch.py` – orchestrates batching logic, using the API module.
  - `utils.py` – shared utilities (logging, retries, config).
  - `main.py` – entry point that ties together batch processing with configurable pipelines.
  - Leverage `Qwen/Qwen3.5-9B` for cheap batch processing and `meta-llama/Llama-3.3-70B-Instruct-Turbo` for complex reasoning tasks.
- **Pending Action:** Implement `src/notebooklm/api.py` with a thin wrapper around NotebookLM endpoints and refactor existing logic from `old_scripts` into the new modules.

## 3. Vault & YAML Discipline
- **Current State:** Vault notes contain a mix of frontmatter styles; some missing required fields like `status: GEM_CHECKED` and `cluster` tags. Several notes lack `source_id` identifiers.
- **Enforcement Rules:** All notes must include the following YAML schema:
  ```yaml
  title: <string>
  date: YYYY-MM-DD
  status: GEM_CHECKED | REVIEW_PENDING
  cluster: H-<num> | G-<num>
  source_id: <UUID>
  tags: [<list>]
  ```
  Validation can be automated via a pre-commit hook that runs a Python script checking frontmatter.

## 4. Registry SOP & Workflow Integration
- **Registry Logic:** The Excel registry maps clusters (G1‑G7) to Prompts (P00‑P09). Each row defines a literature source, its priority (GREEN/YELLOW/RED), and required processing steps.
- **Execution Workflow:**
  1. Identify a GREEN‑priority row.
  2. Run the command:
     ```powershell
     python src/notebooklm/extract_literature.py --excel-path compol_digital_capitalism_vault/RA_NotebookLM_Obsidian_Registry.xlsx --row-id <RowID>
     ```
  3. The script extracts the PDF, runs LLM summarization, and writes an Obsidian note with the enforced YAML frontmatter under `compol_digital_capitalism_vault/notes/`.
  4. Commit the new note and update the registry status column to `Processed`.

## 5. Pending Tasks Matrix (Next 48 Hours)
| Priority | Domain | Task Description | Target Location |
| :--- | :--- | :--- | :--- |
| **P0** | NotebookLM Architecture | Implement `api.py` and refactor legacy scripts into new modules | src/notebooklm/api.py |
| **P1** | YAML Validation | Add pre‑commit hook for vault note frontmatter validation | .git/hooks/pre-commit |
| **P1** | Registry Automation | Write `extract_literature.py` to process Excel rows into notes | src/notebooklm/extract_literature.py |

## 6. Context Gaps
- Detailed content of the legacy scripts in `src/notebooklm/old_scripts` was not examined; review may reveal additional reusable functions.
- Exact schema of existing vault notes to compare against the proposed YAML.
- Access to the Excel registry file (`RA_NotebookLM_Obsidian_Registry.xlsx`) to verify column names and data types.