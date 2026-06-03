# SESSION HANDOFF & CONTEXT RESTORE: COMPOL Digital Capitalism Project

**User:** Diego Polanco (Department of Economics, UMass Amherst)
**Project:** COMPOL_DigitalCapitalism (Analyzing 2021 Presidential Election Facebook Ads data through heterodox macroeconomics, digital capitalism, and political economy).
**Current Date:** June 2, 2026

## 🎯 CURRENT PROJECT STATE (What we have accomplished):
1. **Repository Unified:** Created a clean, reproducible structure at `C:\ReposGitHub\COMPOL_DigitalCapitalism` with `vault/`, `data/`, `literature/`, `src/`, `output/`, and `legacy_repo/`.
2. **Terminal AI Configured:** Successfully bypassed the hardcoded Alibaba DashScope in the `qwen` CLI. The terminal is now correctly routing to **Together.ai** (`https://api.together.ai/v1`) using the `meta-llama/Llama-3.3-70B-Instruct-Turbo` model, with access to `Qwen/Qwen3.5-9B` (for cheap batch processing) and `Qwen/Qwen3.5-397B-A17B` (for complex reasoning).
3. **Manifest Curated:** Updated `literature/pdf_manifest.csv` to include an `include_in_review` boolean column, explicitly excluding administrative files (FrontMatter, TableContents, Index, etc.) and the misplaced `LICHT_2022...pdf`.
4. **Scripts Drafted:** 
   - `src/utils/qwen_cli.py`: A flexible terminal wrapper for Together.ai.
   - `src/notebooklm/extract_literature.py`: A pipeline to read the manifest, extract the first 5 pages of PDFs, query Together.ai with a strict academic prompt, and output structured Markdown with YAML frontmatter directly to `vault/10_Literature/`.
5. **Literature Assessed:** Analyzed Fuchs & Chandler (2019) "Digital Objects, Digital Subjects". Identified key hooks: "Big Data capitalism", "algorithmic knowledge", "digital labour", and the tension between digital optimism/pessimism. Targeted chapters for extraction include Gerbaudo (Platform Party), Dean (Communicative Capitalism), and Fuchs (Beyond Big Data).

## 📂 KEY FILE PATHS TO REMEMBER:
- Repo Root: `C:\ReposGitHub\COMPOL_DigitalCapitalism`
- Manifest: `C:\ReposGitHub\COMPOL_DigitalCapitalism\literature\pdf_manifest.csv`
- PDFs: `C:\ReposGitHub\COMPOL_DigitalCapitalism\literature\pdfs\` (includes `CHANDLER_FUCHS_eds\` subfolder)
- Legacy Scripts to Review: `C:\ReposGitHub\Financialization_LandRent\05_scripts`
- Obsidian Vault Notes: `C:\ReposGitHub\COMPOL_DigitalCapitalism\vault\20_Project_Notes\`

## 🚀 IMMEDIATE NEXT STEPS (Where we left off):
1. **Review Legacy Scripts:** I need to review the Python scripts from `C:\ReposGitHub\Financialization_LandRent\05_scripts` to extract any unique `notebooklmpy` logic, API handling, or best practices to merge into the new `extract_literature.py`.
2. **Align with Vault Notes:** Cross-reference the extraction prompt with the pending notes in `vault/20_Project_Notes/` (Introduction, Conceptual Framework, Analytical Framework, Data Methods) and the user's question registry to ensure the LLM targets specific research gaps.
3. **Test Run:** Execute a small test batch (2-3 PDFs) using: 
   `python src/notebooklm/extract_literature.py --model "Qwen/Qwen3.5-9B"` 
   to verify the Obsidian Markdown output format before running the full manifest.

## 💡 INSTRUCTIONS FOR THE AI:
- Acknowledge this context.
- Ask me to upload or paste the code from the `Financialization_LandRent\05_scripts` folder so we can finalize the `extract_literature.py` protocol.
- Maintain a rigorous, academic, and efficient tone. Prioritize reproducible data science practices and cost-optimized LLM usage (as per my Together.ai Obsidian note).