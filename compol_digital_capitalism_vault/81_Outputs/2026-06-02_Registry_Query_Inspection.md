# COMPOL Digital Capitalism — Registry Query Inspection Report
**Date:** 2026-06-02  
**Source:** `RA_NotebookLM_Obsidian_Registry.xlsx` (Registry sheet + Prompt_Bank sheet)  
**PDF Manifest:** `pdf_manifest.csv` (67 PDFs)  
**Status:** Pre-execution analysis only.

---

## 1. Registry Summary

| Metric | Value |
|---|---|
| Total PDFs registered | 67 |
| Total PDFs in pdf_manifest.csv | 67 |
| All `RA_status` | Not Started (100%) |
| GREEN checkpoint flag | 31 |
| YELLOW checkpoint flag | 36 |
| High priority | 26 |
| Medium priority | 31 |
| Review priority | 6 |
| Low priority | 4 |

### Cluster distribution (primary)

| Cluster ID | Cluster Name | PDF Count |
|---|---|---|
| G6 | DIGITAL_CAPITALISM_PLATFORM_POWER | 19 |
| G4 | CHILE_LATAM_CASE_CONTEXT | 17 |
| G3 | PLATFORMIZATION_DIGITAL_POLITICS | 13 |
| G2 | TOPIC_MODELING_METHOD | 9 |
| G1 | PAID_ADS_OBJECT | 5 |
| G5 | ETHICS_MANIPULATION_RISK | 3 |
| AUX | METADATA_OR_FRONTMATTER | 1 |

### NotebookLM notebooks mapped in registry

| Notebook ID | Cluster coverage |
|---|---|
| NB01_Paid_Digital_Ads | G1_PAID_ADS_OBJECT |
| NB02_Topic_Modeling_Methods | G2_TOPIC_MODELING_METHOD |
| NB03_Platformization_Digital_Politics | G3_PLATFORMIZATION_DIGITAL_POLITICS |
| NB04_Chile_LatAm_Context | G4_CHILE_LATAM_CASE_CONTEXT |
| NB05_Ethics_Manipulation_Risk | G5_ETHICS_MANIPULATION_RISK |
| NB06_Digital_Capitalism_Platform_Power | G6_DIGITAL_CAPITALISM_PLATFORM_POWER |

---

## 2. Prompt Bank — Full Prompt Reference

The `Prompt_Bank` sheet contains 10 prompts (P00–P09). These are assembled per-source by reading the `prompt_ids_to_run` column.

### P00 — Universal Source Extraction *(always applied)*
Extracts: bibliographic identity, what the source studies, method and corpus, core claims, relevance to Diego's paper, cluster tags, possible citation uses, limits, open questions.

### P01 — Paid Ads Object
Extracts: whether source studies paid ads or organic posts, platform, targeting mechanism, ad visibility, disclosure, persuasion, segmentation, audience control.

### P02 — Topic Modeling Method
Extracts: method type (LDA/STM/BERTopic/etc.), corpus, validation strategy, preprocessing choices, Spanish/short-text/political-ad text handling, method limitations, how to cite.

### P03 — Platformization of Digital Politics
Extracts: concept of digitalization/platformization/datafication, actors, platform framing (channel vs. infrastructure), geographic scope, mechanisms linking platforms to campaign strategy, Chile 2021 bridge sentence.

### P04 — Chile / LatAm Context
Extracts: country/election studied, Chile 2019 uprising / constitutional process / party fragmentation / candidate references, LatAm distinctiveness, platforms used, contrast case for Chile 2021, justification sentence for Chile as theoretical case.

### P05 — Ethics / Manipulation Risk
Extracts: risks named (manipulation/privacy/polarization/etc.), empirical evidence vs. speculation, whether microtargeting is inherently harmful or over-feared, platform/campaign/regulator roles, counterargument, ethics/evidence debate framing sentence.

### P06 — Digital Capitalism / Platform Power
Extracts: theoretical object (platform capitalism/digital labor/data extraction/etc.), power mechanism, how source theorizes political advertising as platform-mediated infrastructure, portable concepts, what to exclude, 3 conceptual building blocks.

### P07 — Venue Precedent
Extracts: journal, year, article type, niche coverage (method/object/region/case/theory/platform/venue), relationship to Diego's paper (competitor/analogue/precedent/background), gap remaining after this source, one-sentence citation use.

### P08 — ChatGPT / Qwen Normalize to Obsidian *(applied by Together.ai, not NotebookLM)*
Converts raw NotebookLM output into structured Obsidian note with strict YAML frontmatter + section headers. Applied as normalization step after NotebookLM extraction.

### P09 — 30-Minute Checkpoint Packet
Produces: PDFs processed, notes created/updated, cluster assignments, yellow cases, red cases, claims needing verification, next 30-min plan. **Not used per-source — used for session summaries.**

---

## 3. GREEN + HIGH Priority Queue (25 sources — first batch to process)

These are the sources `extract_hybrid.py` will process first when no `--source_id` is specified (filter: `RA_status == "Not Started"` AND `checkpoint_flag == "GREEN"` AND `primary_cluster != "AUX_METADATA_OR_FRONTMATTER"`).

| source_id | Filename | Primary Cluster | Assigned Notebook | Prompts to Run |
|---|---|---|---|---|
| PDF_003 | ARGOTE_ETAL_2025.pdf | G4_CHILE_LATAM | NB04_Chile_LatAm_Context | P00 + P04 + P02 + P07 |
| PDF_005 | ARUGUETE_ETAL_2024.pdf | G4_CHILE_LATAM | NB04_Chile_LatAm_Context | P00 + P04 + P02 + P07 |
| PDF_006 | BOSSETTA_2020.pdf | G1_PAID_ADS | NB01_Paid_Digital_Ads | P00 + P01 + P03 |
| PDF_011 | CHAGAS_2022.pdf | G4_CHILE_LATAM | NB04_Chile_LatAm_Context | P00 + P04 + P03 |
| PDF_013 | DOBBER_ETAL_2020.pdf | G5_ETHICS | NB05_Ethics | P00 + P05 + P01 |
| PDF_022 | ITUASSU_2023.pdf | G4_CHILE_LATAM | NB04_Chile_LatAm_Context | P00 + P04 + P03 |
| PDF_024 | KANGASLAHTI_2026.pdf | G2_TOPIC_MODEL | NB02_Topic_Modeling | P00 + P02 + P07 |
| PDF_026 | LEERSSEN_ETAL_2023.pdf | G1_PAID_ADS | NB01_Paid_Digital_Ads | P00 + P01 + P05 |
| PDF_027 | LOPEZ-ESCARENA_ETAL_2025.pdf | G4_CHILE_LATAM | NB04_Chile_LatAm_Context | P00 + P04 + P03 |
| PDF_033 | OLOF-LARSSON_ETAL_2025.pdf | G3_PLATFORM | NB03_Platformization | P00 + P03 + P07 + P02 |
| PDF_034 | ORCHARD_ETAL_2024.pdf | G4_CHILE_LATAM | NB04_Chile_LatAm_Context | P00 + P04 + P07 |
| PDF_035 | OSNABRUGGE_ETAL_2023.pdf | G2_TOPIC_MODEL | NB02_Topic_Modeling | P00 + P02 + P07 |
| PDF_037 | PALLISTER_2024.pdf | G4_CHILE_LATAM | NB04_Chile_LatAm_Context | P00 + P04 + P07 + P01 |
| PDF_040 | THEOCHARIS_ETAL_2021.pdf | G3_PLATFORM | NB03_Platformization | P00 + P03 + P02 + P07 |
| PDF_043 | VRIELINK_ETAL_2025.pdf | G1_PAID_ADS | NB01_Paid_Digital_Ads | P00 + P01 + P05 + P07 |
| PDF_044 | WANG_2024.pdf | G2_TOPIC_MODEL | NB02_Topic_Modeling | P00 + P02 + P07 |
| PDF_045 | WIRSCHING_ETAL_2025.pdf | G2_TOPIC_MODEL | NB02_Topic_Modeling | P00 + P02 + P07 |
| PDF_051 | Chandler-DigitalGovernanceAnthropocene-2019.pdf | G6_DIGCAP | NB06_Digital_Capitalism | P00 + P06 + P03 |
| PDF_052 | Chandler-StakeCritiqueBig-2019.pdf | G6_DIGCAP | NB06_Digital_Capitalism | P00 + P06 + P03 |
| PDF_057 | Fuchs-AppropriationDigitalMachines-2019.pdf | G6_DIGCAP | NB06_Digital_Capitalism | P00 + P06 + P03 |
| PDF_058 | Fuchs-BeyondBigData-2019.pdf | G6_DIGCAP | NB06_Digital_Capitalism | P00 + P06 + P03 |
| PDF_059 | Fuchs-Introduction-2019.pdf | G6_DIGCAP | NB06_Digital_Capitalism | P00 + P06 + P03 |
| PDF_060 | Fuchs-KarlMarxAge-2019.pdf | G6_DIGCAP | NB06_Digital_Capitalism | P00 + P06 + P03 |
| PDF_061 | Gerbaudo-PlatformParty-2019.pdf | G6_DIGCAP | NB06_Digital_Capitalism | P00 + P06 + P03 |
| PDF_068 | Negri-AppropriationFixedCapital-2019.pdf | G6_DIGCAP | NB06_Digital_Capitalism | P00 + P06 + P03 |

**Note:** `extract_hybrid.py` does NOT filter by `priority == "High"` in its default logic — it only filters on `RA_status == "Not Started"` AND `checkpoint_flag == "GREEN"`. This means it will run **31** sources (all GREEN), not just the 25 above.

`extract_literature.py` DOES filter by `priority == "High"` in addition — so it runs **26** sources on first pass.

---

## 4. YELLOW Sources (36 — next batch after GREEN)

These require review before processing but are in the queue. They are **not run** in the first pass by either script.

| source_id | Filename | Primary Cluster | Priority | Review Note |
|---|---|---|---|---|
| PDF_001 | ALVAREZ-FUENTES_ETAL_2024.pdf | G4_CHILE_LATAM | Review | Verify exact object |
| PDF_002 | ANSTEAD_ETAL_2025.pdf | G1_PAID_ADS | Review | Verify exact object |
| PDF_004 | ARNAUDO_2017.pdf | G6_DIGCAP | Medium | — |
| PDF_007 | CASEY_ETAL_2023.pdf | G3_PLATFORM | Medium | — |
| PDF_008 | CASTRO_ETAL_2023.pdf | G4_CHILE_LATAM | Medium | — |
| PDF_009 | CERVI_2021.pdf | G3_PLATFORM | Medium | — |
| PDF_010 | CESUR_ETAL_2024.pdf | G4_CHILE_LATAM | Medium | — |
| PDF_012 | DIGITAL_COMPASS_REPORT.pdf | AUX | Low | Metadata/frontmatter only |
| PDF_014 | DVIR-GVIRSMAN_2019.pdf | G3_PLATFORM | Medium | — |
| PDF_015 | ENGEL_2024.pdf | G6_DIGCAP | Medium | — |
| PDF_016 | ESTEVE_DEL_VALLE_ETAL_2021.pdf | G3_PLATFORM | Medium | — |
| PDF_017 | FEENSTRA_ETAL_2022.pdf | G4_CHILE_LATAM | Medium | — |
| PDF_018 | FERNANDEZ_GARCIA_2017.pdf | G4_CHILE_LATAM | Medium | — |
| PDF_019 | GERLITZ_HELMOND_2013.pdf | G6_DIGCAP | Medium | — |
| PDF_020 | GILARDI_ETAL_2022.pdf | G3_PLATFORM | Medium | — |
| PDF_021 | GOLDEN_ETAL_2024.pdf | G1_PAID_ADS | Medium | — |
| PDF_023 | JURGENS_JUNGHERR_2024.pdf | G4_CHILE_LATAM | Medium | — |
| PDF_025 | KREISS_MCGREGOR_2018.pdf | G1_PAID_ADS | Medium | — |
| PDF_028 | LUKITO_2019.pdf | G4_CHILE_LATAM | Medium | — |
| PDF_029 | LUNA_ETAL_2022_CHILE.pdf | G4_CHILE_LATAM | Low | — |
| PDF_030 | MAURER_ETAL_2023.pdf | G3_PLATFORM | Medium | — |
| PDF_031 | NICHOLS_ETAL_2020.pdf | G2_TOPIC_MODEL | Medium | — |
| PDF_032 | OLOF-LARSSON_2020.pdf | G3_PLATFORM | Medium | — |
| PDF_036 | PACHECO_2024.pdf | G4_CHILE_LATAM | Review | — |
| PDF_038 | PENUCCI_2024.pdf | G4_CHILE_LATAM | Review | — |
| PDF_039 | SCHMOKEL_ETAL_2022.pdf | G3_PLATFORM | Medium | — |
| PDF_041 | THORSON_ETAL_2019.pdf | G1_PAID_ADS | Medium | — |
| PDF_042 | UNULU_2024.pdf | G3_PLATFORM | Medium | — |
| PDF_046 | YANG_ETAL_2023.pdf | G3_PLATFORM | Medium | — |
| PDF_047 | ZHAO_ETAL_2024.pdf | G3_PLATFORM | Review | — |
| PDF_049 | Boehnert-2019.pdf | G6_DIGCAP | Medium | — |
| PDF_050 | Brighi-2019.pdf | G6_DIGCAP | Medium | — |
| PDF_053 | Cowley-2019.pdf | G6_DIGCAP | Medium | — |
| PDF_054 | Dean-2019.pdf | G6_DIGCAP | Medium | — |
| PDF_062 | Goodwin-2019.pdf | G6_DIGCAP | Medium | — |
| PDF_064 | Jarrett-2019.pdf | G6_DIGCAP | Medium | — |
| PDF_065 | Kavada-2019.pdf | G6_DIGCAP | Medium | — |
| PDF_066 | LICHT_2022.pdf | G2_TOPIC_MODEL | Medium | — |
| PDF_067 | Moore-2019.pdf | G6_DIGCAP | Medium | — |
| PDF_069 | Qiu-2019.pdf | G6_DIGCAP | Medium | — |
| PDF_070 | Rekret-2019.pdf | G6_DIGCAP | Medium | — |
| PDF_072 | Tambakaki-2019.pdf | G6_DIGCAP | Medium | — |

---

## 5. Prompt Combination Analysis

The registry defines prompt combinations per source. Here are all unique prompt combinations observed:

| Prompt Combination | Count | Cluster(s) |
|---|---|---|
| P00 + P06 + P03 | 15 | G6 DIGCAP |
| P00 + P04 + P03 | 6 | G4 CHILE_LATAM |
| P00 + P02 + P07 | 5 | G2 TOPIC_MODEL |
| P00 + P04 + P02 + P07 | 2 | G4+G2 cross |
| P00 + P04 + P07 | 2 | G4 CHILE_LATAM |
| P00 + P01 + P03 | 2 | G1 PAID_ADS + G3 PLATFORM |
| P00 + P01 + P05 + P07 | 2 | G1+G5 cross |
| P00 + P03 + P02 + P07 | 2 | G3+G2 cross |
| P00 + P03 + P05 + P07 | 2 | G3+G5 cross |
| P00 + P01 + P05 | 1 | G1+G5 |
| P00 + P05 + P01 | 1 | G5+G1 |
| P00 + P04 + P07 + P01 | 1 | G4+G1 cross |
| P00 + P03 + P05 | 1 | G3+G5 |
| P00 + P03 + P07 + P02 | 1 | G3+G2 cross |
| P00 + P04 + P03 + P07 | 1 | G4+G3 cross |

**P00 is universal** — applied to every single source (67/67).  
**P08 is never in `prompt_ids_to_run`** — it is applied by `extract_hybrid.py` as a post-processing step.

---

## 6. PDF Manifest Cross-Reference

The `pdf_manifest.csv` lists 67 PDFs in two locations:
- **ROOT folder** (46 files): `AUTHOR_YEAR.pdf` format, stored flat in the `literature/` directory
- **CHANDLER_FUCHS_eds subfolder** (21 files): Chapters from the Chandler & Fuchs edited volume (2019)

### ROOT PDFs (flat) — sample
`ALVAREZ-FUENTES_ETAL_2024.pdf`, `ANSTEAD_ETAL_2025.pdf`, `ARGOTE_ETAL_2025.pdf`, `ARNAUDO_2017.pdf`, `ARUGUETE_ETAL_2024.pdf`, `BOSSETTA_2020.pdf`, `CASEY_ETAL_2023.pdf`, `CASTRO_ETAL_2023.pdf`, `CERVI_2021.pdf`, `CESUR_ETAL_2024.pdf`, `CHAGAS_2022.pdf`, `DOBBER_ETAL_2020.pdf`, `DVIR-GVIRSMAN_2019.pdf`, `ENGEL_2024.pdf`, `ESTEVE_DEL_VALLE_ETAL_2021.pdf`, `FEENSTRA_ETAL_2022.pdf`, `FERNANDEZ_GARCIA_2017.pdf`, `GERLITZ_HELMOND_2013.pdf`, `GILARDI_ETAL_2022.pdf`, `GOLDEN_ETAL_2024.pdf`, `ITUASSU_2023.pdf`, `JURGENS_JUNGHERR_2024.pdf`, `KANGASLAHTI_2026.pdf`, `KREISS_MCGREGOR_2018.pdf`, `LEERSSEN_ETAL_2023.pdf`, `LOPEZ-ESCARENA_ETAL_2025.pdf`, `LUKITO_2019.pdf`, `LUNA_ETAL_2022_CHILE.pdf`, `MAURER_ETAL_2023.pdf`, `NICHOLS_ETAL_2020.pdf`, `OLOF-LARSSON_2020.pdf`, `OLOF-LARSSON_ETAL_2025.pdf`, `ORCHARD_ETAL_2024.pdf`, `OSNABRUGGE_ETAL_2023.pdf`, `PACHECO_2024.pdf`, `PALLISTER_2024.pdf`, `PENUCCI_2024.pdf`, `SCHMOKEL_ETAL_2022.pdf`, `THEOCHARIS_ETAL_2021.pdf`, `THORSON_ETAL_2019.pdf`, `UNULU_2024.pdf`, `VRIELINK_ETAL_2025.pdf`, `WANG_2024.pdf`, `WIRSCHING_ETAL_2025.pdf`, `YANG_ETAL_2023.pdf`, `ZHAO_ETAL_2024.pdf`

### CHANDLER_FUCHS_eds subfolder PDFs (21 files)
All 2019 chapters, assigned to `G6_DIGITAL_CAPITALISM_PLATFORM_POWER`:
`Boehnert-ContradictionsTwitterSocial-2019.pdf`, `Brighi-BeyondRepression-2019.pdf`, `Chandler-DigitalGovernanceAnthropocene-2019.pdf`, `Chandler-StakeCritiqueBig-2019.pdf`, `Cowley-PosthumanismSpectrum-2019.pdf`, `Dean-CritiqueCollectivity-2019.pdf`, `Fuchs-AppropriationDigitalMachines-2019.pdf`, `Fuchs-BeyondBigData-2019.pdf`, `Fuchs-Introduction-2019.pdf`, `Fuchs-KarlMarxAge-2019.pdf`, `Gerbaudo-PlatformParty-2019.pdf`, `Goodwin-WageWorkersSlaves-2019.pdf`, `Jarrett-ReproductiveLens-2019.pdf`, `Kavada-MovementParty-2019.pdf`, `LICHT_2022_cross-lingual_text_classification_OSF.pdf`, `Moore-EaffectivePrecarityControl-2019.pdf`, `Negri-AppropriationFixedCapital-2019.pdf`, `Qiu-GoodbyeiSlave-2019.pdf`, `Rekret-SeeingLikeCyborg-2019.pdf`, `Tambakaki-SubjectsContextsModes-2019.pdf`

> **⚠️ Path Issue:** The `relative_path` column in the registry uses Windows backslash paths (e.g., `CHANDLER_FUCHS_eds\Boehnert-ContradictionsTwitterSocial-2019.pdf`). The script constructs `pdf_path = Path(pdf_dir) / relative_path`. On Windows this should work correctly. If running on Linux/Mac, the backslash will cause failures.

---

## 7. Output Note Locations

Each registry row defines `output_obsidian_note` (the filename for the generated Obsidian note). All outputs go to the `output_dir` argument passed at runtime, typically:

```
compol_digital_capitalism_vault\10_Literature\PDF_001_ALVAREZ-FUENTES_ETAL_2024.md
compol_digital_capitalism_vault\10_Literature\PDF_002_ANSTEAD_ETAL_2025.md
...
compol_digital_capitalism_vault\10_Literature\PDF_072_Tambakaki-SubjectsContextsModes-2019.md
```

---

## 8. Runtime Estimates

| Scenario | Time per source | Total for 31 GREEN sources |
|---|---|---|
| `extract_hybrid.py` (NotebookLM + Qwen) | ~3–8 min/source | ~1.5–4 hours |
| `extract_literature.py` (Qwen only) | ~30–60 sec/source | ~15–30 min |

NotebookLM time dominated by: PDF upload + indexing time (`add_source_and_wait`), which varies by PDF size (0.28 MB to 6.55 MB).

---

## 9. Recommended Processing Strategy

```
Phase 1 — Dry run (1 source):
  python -m src.notebooklm.extract_hybrid --source_id PDF_059
  (Fuchs-Introduction-2019.pdf: smallest of the G6 DIGCAP batch at ~1 MB)

Phase 2 — G6 batch (10 GREEN sources, all Chandler_Fuchs_eds):
  PDF_051, PDF_052, PDF_057, PDF_058, PDF_059, PDF_060, PDF_061, PDF_068
  Reason: same notebook (NB06), same prompts (P00+P06+P03), batches efficiently

Phase 3 — G4 Chile/LatAm batch (7 GREEN sources):
  PDF_003, PDF_005, PDF_011, PDF_022, PDF_027, PDF_034, PDF_037

Phase 4 — G2 Topic Modeling batch (5 GREEN sources):
  PDF_024, PDF_035, PDF_044, PDF_045 + PDF_066

Phase 5 — G3 Platformization batch (2 GREEN):
  PDF_033, PDF_040

Phase 6 — G1 Paid Ads batch (3 GREEN):
  PDF_006, PDF_026, PDF_043

Phase 7 — G5 Ethics batch (1 GREEN):
  PDF_013

Phase 8 — YELLOW sources (after Diego review of flagged cases)
```
