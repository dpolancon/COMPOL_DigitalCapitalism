#!/usr/bin/env python3
"""
Auto-generate Obsidian-ready question templates for all 98 per-paper questions.
Reads directly from your Excel registry and creates notes/questions/PDFXXX_QYY.md files.
"""

import pandas as pd
from pathlib import Path

# Configuration
EXCEL_PATH = "02_LitRev_Sistematica/land_rent_financialization_literature_registry.xlsx"
OUTPUT_DIR = Path("notes/questions")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Load registry sheets
xls = pd.ExcelFile(EXCEL_PATH)
papers_df = pd.read_excel(xls, sheet_name="01_Paper_Registry")
questions_df = pd.read_excel(xls, sheet_name="02_PerPaper_Questions")
clusters_df = pd.read_excel(xls, sheet_name="03_Clusters")

# Build lookup dictionaries
paper_map = papers_df.set_index("Source ID").to_dict("index")
cluster_map = dict(zip(clusters_df["Cluster ID"], clusters_df["Cluster name"]))

print(f"📊 Found {len(questions_df)} questions. Generating templates...\n")

created = 0
skipped = 0

for _, q in questions_df.iterrows():
    qid = q["Question ID"]
    source_id = q["Source ID"]
    paper = paper_map.get(source_id, {})
    cluster_id = paper.get("Cluster ID", "Unknown")
    cluster_name = cluster_map.get(cluster_id, "Unknown")

    file_path = OUTPUT_DIR / f"{qid}.md"
    if file_path.exists():
        print(f"️  Skipping {qid} (already exists)")
        skipped += 1
        continue

    # 1. YAML Frontmatter
    yaml_fm = f"""---
note_id: "{qid}"
note_type: "notebooklm_per_paper_question"
status: "template_generated"
source_id: "{source_id}"
question_id: "{qid}"
paper_title: "{paper.get('Title', 'N/A')}"
authors: "{paper.get('Authors', 'N/A')}"
year: {int(paper.get('Year', 0)) if pd.notna(paper.get('Year')) else 'N/A'}
venue: "{paper.get('Publication venue / status', 'N/A')}"
cluster_id: "{cluster_id}"
cluster_name: "{cluster_name}"
question_tag: "{q['Question tag']}"
use: "NotebookLM answer; then paste distilled note into Obsidian"
---
"""

    # 2. Markdown Body
    md_body = f"""# {qid}

## Source

- Source ID: `{source_id}`
- Paper: {paper.get('Title', 'N/A')}
- Authors: {paper.get('Authors', 'N/A')}
- Year: {paper.get('Year', 'N/A')}
- Venue/status: {paper.get('Publication venue / status', 'N/A')}
- Cluster: `{cluster_id}`

## NotebookLM question

{q['NotebookLM question']}

## NotebookLM answer

> *[PASTE NOTEBOOKLM ANSWER HERE OR LEAVE FOR QWEN TO DRAFT]*

## Distilled note

- **Core claim**: *[QWEN/USER TO FILL]*
- **Mechanism**: 
  - *[BULLET 1]*
  - *[BULLET 2]*
  - *[BULLET 3]*
- **Formal object/result, if any**: *[THEOREM/PROPOSITION OR N/A]*
- **Relevance for the project memo**: *[HOW THIS ANSWERS PROJECT QUESTIONS]*
- **Critical caveat**: *[LIMITATION FOR LATIN AMERICAN CONTEXTS]*

## Evidence / page anchors

- Page(s): `[UNKNOWN]`
- Key passage(s), paraphrased or short quote only: *[≤50 WORDS]*

## Links

- Source paper note: [[{source_id}]]
- Cluster note: [[{cluster_id}]]
- Question index: [[I02_per_paper_question_index#{qid}]]

## Next action

- [ ] Run/paste NotebookLM answer
- [ ] Distill answer
- [ ] Add evidence anchors
- [ ] Link to cluster synthesis
"""

    # 3. Write file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(yaml_fm + md_body)
    print(f"✅ Created: {file_path.name}")
    created += 1

print(f"\n Done! {created} templates generated | {skipped} skipped (already exist)")
print(f"📁 Output: {OUTPUT_DIR.resolve()}")
print("\n🔄 Next step: Use Qwen/Continue to batch-fill answers, or run NotebookLM queries.")