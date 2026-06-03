# COMPOL Digital Capitalism — Repo Structure & NotebookLM Pipeline Report
**Date:** 2026-06-02  
**Prepared by:** Antigravity (Agentic AI)  
**Status:** Pre-execution planning only — no scripts have been run.

---

## 1. Repository Overview

```
C:\ReposGitHub\COMPOL_DigitalCapitalism\
├── .env                              ← API key (Together.ai / OPEN_API_KEY)
├── .gitignore
├── requirements.txt                  ← Python dependencies
├── setup_repo.ps1                    ← PowerShell bootstrap script
│
├── compol_digital_capitalism_vault\  ← Obsidian vault root
│   ├── 10_Literature\
│   │   ├── RA_NotebookLM_Obsidian_Registry.xlsx  ← Master registry (3 sheets)
│   │   └── pdf_manifest.csv                       ← 67 PDFs listed
│   ├── 80_Prompts\
│   │   ├── PROMPT_01_FIRST_PASS_AUDIT_AND_CURATION.md
│   │   └── PROMPT_02_EXECUTE_EXTERNAL_PROMPT.md
│   └── 81_Outputs\                   ← All generated reports go here
│
├── src\
│   └── notebooklm\                   ← Main automation package
│       ├── __init__.py
│       ├── api.py                    ← Together.ai (Qwen) LLM wrapper
│       ├── notebooklm_cli.py         ← notebooklm-py CLI wrapper
│       ├── extract_literature.py     ← Together.ai-only pipeline (no NotebookLM)
│       ├── extract_hybrid.py         ← Hybrid: NotebookLM extract → Qwen normalize
│       ├── utils.py                  ← Shared utilities (prompts, YAML, .env)
│       └── old_scripts\              ← Legacy scripts (19 files, reference only)
│           ├── fetch_notebooklm_answers.py   ← Core legacy fetch logic
│           ├── fetch_cluster_notebooklm_answers.py
│           ├── save_notes_batch.py
│           ├── parse_registry.py
│           ├── generate_paper_notes.py
│           ├── build_cluster_evidence_map.py
│           ├── build_phase3a_synthesis_artifacts.py
│           ├── validate_phase2_clusters.py
│           ├── validate_phase3a_synthesis.py
│           └── ... (10 more utility/batch scripts)
│
├── data\                             ← Raw data directory
├── literature\                       ← PDF storage root (67 PDFs)
├── output\                           ← Analysis outputs
└── zip_files\                        ← Compressed archives
```

---

## 2. External Library: `notebooklm-py` (teng-lin/notebooklm-py)

**Repository:** https://github.com/teng-lin/notebooklm-py  
**PyPI package:** `notebooklm-py`  
**Nature:** Unofficial Python API + CLI for Google NotebookLM. Uses undocumented Google internal APIs. Google may change them without notice.

### What it provides

| Capability | Detail |
|---|---|
| **Notebooks** | Create, list, rename, delete |
| **Sources** | Add PDFs, URLs, YouTube, Google Drive, pasted text; wait for indexing |
| **Chat / Ask** | Ask questions against indexed sources; use `--source` to pin specific sources |
| **Research** | Web/Drive research agents with auto-import |
| **Content generation** | Audio overview, video, slides, quiz, flashcards, report, mind map, data table |
| **Downloads** | Batch download artifacts (MP3, MP4, PDF, PPTX, PNG, CSV, JSON, Markdown) |
| **Sharing** | Public/private links, viewer/editor permissions |

### Key CLI commands used by this repo

```powershell
# Authentication
notebooklm login              # Browser-based OAuth login
notebooklm auth check --test --json   # Verify auth works

# Notebooks
notebooklm notebook create "My Notebook"
notebooklm notebook use <notebook_id>
notebooklm notebook delete <notebook_id> --yes

# Sources
notebooklm source add <file_or_url> --wait   # --wait blocks until indexing complete

# Ask / Query
notebooklm ask --prompt-file prompt.txt --json
notebooklm ask --notebook <id> --source <source_id> --json --timeout 120

# JSON output
# All commands support --json flag for machine-readable output
```

### Install commands
```powershell
pip install "notebooklm-py[browser]"    # includes Playwright for browser auth
playwright install chromium              # download browser driver for login flow
notebooklm login                        # interactive browser OAuth
notebooklm auth check --test --json     # validate
```

---

## 3. The Two Execution Pipelines

The repo implements **two alternative pipelines**. The choice depends on whether you have `notebooklm-py` installed and authenticated.

### Pipeline A — `extract_hybrid.py` (Recommended for NotebookLM)
**Full hybrid: NotebookLM extracts from PDFs → Qwen normalizes to Obsidian format**

```
Registry (Excel) → filter GREEN/Not Started rows
    ↓
For each PDF:
    notebooklm_cli.py: create_notebook() → add_source_and_wait() → ask(P00+PX prompts)
    ↓
Raw NotebookLM answer
    ↓
Together.ai (Qwen): apply P08_CHATGPT_NORMALIZE_TO_OBSIDIAN prompt
    ↓
Obsidian .md note saved to output_dir
    ↓
Registry updated: RA_status = "Saved in Obsidian"
```

**Execution command:**
```powershell
python -m src.notebooklm.extract_hybrid `
  --excel_path "compol_digital_capitalism_vault\10_Literature\RA_NotebookLM_Obsidian_Registry.xlsx" `
  --pdf_dir "literature" `
  --output_dir "compol_digital_capitalism_vault\10_Literature" `
  --model "Qwen/Qwen3.5-9B"

# Single source:
python -m src.notebooklm.extract_hybrid `
  --excel_path "..." --pdf_dir "..." --output_dir "..." `
  --source_id PDF_003
```

### Pipeline B — `extract_literature.py` (Together.ai only, no NotebookLM)
**Simpler: extracts PDF text directly via pdfplumber → sends to Qwen**

```
Registry (Excel) → filter High priority / Not Started rows
    ↓
For each PDF:
    pdfplumber: extract first 5 pages of text
    ↓
Together.ai (Qwen/Llama): apply P00+PX system prompts
    ↓
create_yaml_frontmatter() → combine with LLM response
    ↓
Obsidian .md note saved to output_dir
    ↓
Registry updated: RA_status = "Processed_Pending_Review"
```

**Execution command:**
```powershell
python -m src.notebooklm.extract_literature `
  --excel_path "compol_digital_capitalism_vault\10_Literature\RA_NotebookLM_Obsidian_Registry.xlsx" `
  --pdf_dir "literature" `
  --output_dir "compol_digital_capitalism_vault\10_Literature" `
  --model "Qwen/Qwen3.5-9B"

# Single source:
python -m src.notebooklm.extract_literature `
  --excel_path "..." --pdf_dir "..." --output_dir "..." `
  --source_id PDF_003
```

### Pipeline comparison

| Feature | `extract_hybrid.py` | `extract_literature.py` |
|---|---|---|
| Uses NotebookLM | ✅ Yes (for extraction) | ❌ No |
| Uses Together.ai | ✅ Yes (for P08 normalization) | ✅ Yes (for all prompts) |
| PDF reading | NotebookLM (full document) | pdfplumber (first 5 pages) |
| Output quality | Higher (NotebookLM has full PDF context) | Lower (only first 5 pages) |
| Requires login | ✅ `notebooklm login` | ❌ No |
| Rate limits | Google's NotebookLM limits + Together.ai | Together.ai only |
| Requires registry sheets | `Registry` + `Prompt_Bank` | `Registry` + `Prompt_Bank` |

---

## 4. `utils.py` — Key Functions

| Function | Purpose |
|---|---|
| `load_prompt_registry(excel_path)` | Reads `Prompt_Bank` sheet → `{prompt_id: prompt_text}` dict |
| `parse_prompt_ids(prompt_ids_str)` | Splits `"P00 + P04 + P02"` into `["P00", "P04", "P02"]` |
| `build_extraction_prompt(prompt_ids_str, registry)` | Joins multiple prompt texts (excludes P08) |
| `get_p08_normalization_prompt(registry)` | Returns the Obsidian normalization prompt (P08) |
| `create_yaml_frontmatter(...)` | Generates strict YAML frontmatter for Obsidian vault |
| `load_environment()` | Loads `.env` → `OPEN_API_KEY`, `OPEN_API_BASE` |

---

## 5. `api.py` — TogetherAIClient

```python
client = TogetherAIClient(
    base_url="https://api.together.ai/v1",
    api_key=os.getenv("OPEN_API_KEY")   # loaded from .env
)

# Extract text from PDF (first 5 pages via pdfplumber)
text = client.extract_text("path/to/file.pdf", max_pages=5)

# Query LLM
response = client.query_llm(
    prompt_text=full_prompt,
    model="Qwen/Qwen3.5-9B",   # or "meta-llama/Llama-3.3-70B-Instruct-Turbo"
    max_retries=3
)
```

**⚠️ Bug found:** The env var in `api.py` line 28 reads `OPEN_API_KEY` but the `.env` file also uses `OPEN_API_KEY`. However, `utils.py`'s `load_environment()` function may expect `OPEN_API_BASE` to also be set — currently absent from `.env`. This will cause a `KeyError` at runtime in `extract_hybrid.py` unless `OPEN_API_BASE` is added.

---

## 6. `notebooklm_cli.py` — NotebookLM_CLI Class

```python
nlm = NotebookLM_CLI()           # checks auth on init (raises RuntimeError if not logged in)
nb_id = nlm.create_notebook("Temp_Extract_PDF_003")
nlm.add_source_and_wait(nb_id, "path/to/file.pdf")
raw_answer = nlm.ask(nb_id, prompt_text)
nlm.delete_notebook(nb_id)
```

All commands run `notebooklm <cmd> --json` as a subprocess and parse JSON output.

---

## 7. Known Issues and Pre-Flight Checks

| # | Issue | Impact | Fix Required Before Running |
|---|---|---|---|
| 1 | `notebooklm` CLI not installed | `extract_hybrid.py` fails on init | `pip install "notebooklm-py[browser]"` + `playwright install chromium` |
| 2 | `notebooklm login` not done | `NotebookLM_CLI()` raises RuntimeError | Run `notebooklm login` interactively |
| 3 | `OPEN_API_BASE` missing from `.env` | `extract_hybrid.py` may KeyError | Add `OPEN_API_BASE=https://api.together.ai/v1` to `.env` |
| 4 | `yaml` package not in `requirements.txt` | `utils.py` import fails | `pip install pyyaml` |
| 5 | `pdf_manifest.csv` uses mixed delimiter | Direct CSV read fails without `sep=None` | Use `pd.read_csv(..., sep=None, engine='python')` |
| 6 | `load_environment()` not defined in utils.py | `extract_literature.py` import error | Implement or stub `load_environment()` in `utils.py` |
| 7 | Registry `RA_status` is "Not Started" for all 67 PDFs | Pipeline works, nothing will be skipped | No fix needed — expected fresh state |
| 8 | `extract_hybrid.py` uses `sheet_name='Registry'` | Must match exact sheet name | ✅ Confirmed — sheet name is "Registry" |

---

## 8. Dependencies to Install

### From `requirements.txt` (existing)
```powershell
pip install -r requirements.txt
```
Covers: `pandas`, `numpy`, `openai`, `python-dotenv`, `requests`, `PyPDF2`, `pdfplumber`, `matplotlib`, `seaborn`, `statsmodels`, `jupyter`

### Additional dependencies NOT in requirements.txt

```powershell
# For notebooklm-py CLI (Pipeline A only)
pip install "notebooklm-py[browser]"
playwright install chromium

# For YAML frontmatter generation (used in utils.py)
pip install pyyaml

# For Excel reading (openpyxl backend for pandas)
pip install openpyxl

# Optional: for richer LLM model access
pip install together    # if using Together.ai SDK directly instead of openai-compatible endpoint
```

### Complete updated `requirements.txt` (recommended additions)
```
pandas>=2.0.0
numpy>=1.24.0
openai>=1.0.0
python-dotenv>=1.0.0
requests>=2.31.0
PyPDF2>=3.0.0
pdfplumber>=0.10.0
pyyaml>=6.0.0
openpyxl>=3.1.0
notebooklm-py[browser]>=0.1.0
matplotlib>=3.7.0
seaborn>=0.12.0
statsmodels>=0.14.0
jupyter>=1.0.0
```

---

## 9. `.env` File Required Keys

Current `.env` contains:
```
OPEN_API_KEY=tgp_v1_...
```

**Add missing key:**
```
OPEN_API_KEY=tgp_v1_...
OPEN_API_BASE=https://api.together.ai/v1
```

---

## 10. Recommended Execution Order (Pre-Flight Checklist)

```
[ ] 1. pip install -r requirements.txt
[ ] 2. pip install pyyaml openpyxl "notebooklm-py[browser]"
[ ] 3. playwright install chromium
[ ] 4. Add OPEN_API_BASE to .env
[ ] 5. notebooklm login     (browser will open — complete OAuth)
[ ] 6. notebooklm auth check --test --json     (verify: {"status": "ok"})
[ ] 7. Dry-run single source:
        python -m src.notebooklm.extract_hybrid \
          --excel_path "..." --pdf_dir "literature" \
          --output_dir "compol_digital_capitalism_vault\10_Literature" \
          --source_id PDF_003
[ ] 8. Review output note at: compol_digital_capitalism_vault\10_Literature\PDF_003_ARGOTE_ETAL_2025.md
[ ] 9. If successful, run full GREEN+High batch (25 sources)
```

---

## 11. Legacy Scripts Summary (`old_scripts/`)

These 19 scripts predate the current modular architecture. They are **not runnable as-is** (hardcoded paths, require `registry_parsed.json` that doesn't exist at current paths), but contain valuable reference logic.

| Script | Reusable Logic |
|---|---|
| `fetch_notebooklm_answers.py` | Full `ask_notebooklm()` + `render_note()` output format |
| `fetch_cluster_notebooklm_answers.py` | Cluster-level batch querying |
| `save_notes_batch.py` | Batch note saving with status tracking |
| `parse_registry.py` | Registry JSON parsing patterns |
| `generate_paper_notes.py` | Per-paper note generation |
| `build_cluster_evidence_map.py` | Cluster evidence aggregation |
| `validate_phase2_clusters.py` | Quality validation logic |
| `build_phase3a_synthesis_artifacts.py` | Synthesis document generation (58KB — most complex) |

**Recommendation:** Do not run these. Use `extract_hybrid.py` instead.
