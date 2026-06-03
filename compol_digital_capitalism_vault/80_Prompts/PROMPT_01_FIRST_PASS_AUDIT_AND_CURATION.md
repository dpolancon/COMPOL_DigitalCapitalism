---
prompt_id: PROMPT_01
title: First Pass - Repo Audit, Script Curation & Workflow Setup
date: 2026-06-02
target_output: 81_Outputs/2026-06-02_Pass01_Repo_Audit.md
status: ACTIVE
---

# ROLE & OBJECTIVE
You are the Lead Research Architect and DevOps for the COMPOL_DigitalCapitalism project. Your objective is to conduct a comprehensive "First Pass" audit of the repository, curate legacy automation scripts, and establish strict operational discipline for the Obsidian vault and literature registry.

# CONTEXT & PATHS
- **Repo Root:** `C:\ReposGitHub\COMPOL_DigitalCapitalism`
- **Legacy Scripts:** `C:\ReposGitHub\COMPOL_DigitalCapitalism\src\notebooklm\old_scripts` (Contains previous Python scripts for remote NotebookLM management).
- **Obsidian Vault:** `C:\ReposGitHub\COMPOL_DigitalCapitalism\compol_digital_capitalism_vault`
- **Literature Registry:** `RA_NotebookLM_Obsidian_Registry.xlsx` (Maps 72 PDFs to G1-G7 clusters and P00-P09 prompts).

# INSTRUCTIONS FOR ANALYSIS

## 1. Legacy Script Curation (NotebookLM Automation)
- Scan the contents of `src/notebooklm/old_scripts`.
- Identify reusable logic for managing NotebookLM remotely (e.g., API handling, batching, error management, session handling).
- Propose a modernized, modular Python architecture for `src/notebooklm/` that integrates with our Together.ai terminal routing (using `Qwen/Qwen3.5-9B` for cheap batch processing and `meta-llama/Llama-3.3-70B-Instruct-Turbo` for complex reasoning).

## 2. Vault & YAML Discipline Audit
- Review the current state of the vault notes (specifically the harmonized `H-` notes and the `require_systematize` folder).
- Identify any violations of the established YAML frontmatter schema (e.g., missing `status: GEM_CHECKED`, incorrect `cluster` tags, missing `source_id`).
- Define a strict validation rule for all future literature notes.

## 3. Literature Registry SOP (Standard Operating Procedure)
- Inspect the logic of the `RA_NotebookLM_Obsidian_Registry.xlsx` (Clusters G1-G7, Prompts P00-P09).
- Draft a concise, 1-page SOP on how to use this registry to drive the automated extraction pipeline. How does a row in the Excel sheet translate into a terminal command and an Obsidian note?

# REQUIRED OUTPUT FORMAT
Generate a rigorous, highly structured Markdown report. Do not use conversational filler. The output must be formatted exactly to be saved as `81_Outputs/2026-06-02_Pass01_Repo_Audit.md`.

Use the following structure:

# COMPOL Digital Capitalism: First Pass Audit Report
**Date:** 2026-06-02
**Prompt ID:** PROMPT_01

## 1. Executive Summary
[3-4 sentences summarizing the repo's health and the primary bottlenecks identified.]

## 2. Legacy Script Curation (`src/notebooklm/`)
- **Extracted Logic:** [What is worth saving from `old_scripts`?]
- **Proposed Architecture:** [How should the new `extract_literature.py` be structured?]
- **Pending Action:** [Exact next step to write the code.]

## 3. Vault & YAML Discipline
- **Current State:** [Assessment of current note hygiene.]
- **Enforcement Rules:** [The exact YAML schema that must be enforced.]

## 4. Registry SOP & Workflow Integration
- **Registry Logic:** [Brief summary of how G-clusters and P-prompts map to the paper's gaps.]
- **Execution Workflow:** [Step-by-step guide on how to process a GREEN priority row from the Excel registry into an Obsidian note using the terminal.]

## 5. Pending Tasks Matrix (Next 48 Hours)
| Priority | Domain | Task Description | Target Location |
| :--- | :--- | :--- | :--- |
| **P0** | [Domain] | [Task] | [Path] |
| **P1** | [Domain] | [Task] | [Path] |

## 6. Context Gaps
[List any files or folders you needed to see but were not provided in the context.]