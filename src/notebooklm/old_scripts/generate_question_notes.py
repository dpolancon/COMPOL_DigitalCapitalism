#!/usr/bin/env python3
"""
Generate per-question markdown notes from the Land-Rent Literature Registry.
Each question gets its own file (e.g., PDF001_Q01.md) following the provided template.
"""

import pandas as pd
import os
from pathlib import Path

# Configuration
EXCEL_PATH = "02_LitRev_Sistematica/land_rent_financialization_literature_registry.xlsx"
OUTPUT_DIR = Path("notes/questions")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
OVERWRITE = "--overwrite" in os.sys.argv

# Load Excel sheets
xls = pd.ExcelFile(EXCEL_PATH)
papers_df = pd.read_excel(xls, sheet_name="01_Paper_Registry")
questions_df = pd.read_excel(xls, sheet_name="02_PerPaper_Questions")
clusters_df = pd.read_excel(xls, sheet_name="03_Clusters")

# Create cluster lookup dictionary
cluster_map = dict(zip(clusters_df['Cluster ID'], clusters_df['Cluster name']))

# Index papers by Source ID for fast lookup
papers_df.set_index('Source ID', inplace=True)

print(f"📊 Processing {len(questions_df)} questions from registry...")

for _, q_row in questions_df.iterrows():
    qid = q_row['Question ID']
    source_id = q_row['Source ID']
    
    # Lookup paper metadata
    if source_id not in papers_df.index:
        print(f"⚠️  Warning: Paper {source_id} not found in registry. Skipping {qid}.")
        continue
        
    p_row = papers_df.loc[source_id]
    cluster_id = p_row['Cluster ID']
    cluster_name = cluster_map.get(cluster_id, "Unknown")
    
    # Safe value extraction
    year = int(p_row['Year']) if pd.notna(p_row['Year']) else ""
    venue = p_row['Publication venue / status'] if pd.notna(p_row['Publication venue / status']) else ""
    status = q_row['Status'] if pd.notna(q_row['Status']) else "pending_notebooklm"
    
    # YAML Frontmatter
    yaml_block = f"""---
note_id: "{qid}"
note_type: "notebooklm_per_paper_question"
status: "{status}"
source_id: "{source_id}"
question_id: "{qid}"
paper_title: "{p_row['Title']}"
authors: "{p_row['Authors']}"
year: "{year}"
venue: "{venue}"
cluster_id: "{cluster_id}"
cluster_name: "{cluster_name}"
question_tag: "{q_row['Question tag']}"
use: "{q_row['Expected output / use']}"
---
"""

    # Markdown Body
    md_body = f"""
# {qid}

## Source

- Source ID: `{source_id}`
- Paper: {p_row['Title']}
- Authors: {p_row['Authors']}
- Year: {year}
- Venue/status: {venue}
- Cluster: `{cluster_id}`

## NotebookLM question

{q_row['NotebookLM question']}

## NotebookLM answer

> *[Paste NotebookLM answer here]*

## Distilled note

- Core claim:
- Mechanism:
- Formal object/result, if any:
- Relevance for the project memo:
- Critical caveat:

## Evidence / page anchors

- Page(s):
- Key passage(s), paraphrased or short quote only:

## Links

- Source paper note: [[{source_id}]]
- Cluster note: [[{cluster_id}]]

## Next action

- [ ] Run/paste NotebookLM answer
- [ ] Distill answer
- [ ] Add evidence anchors
- [ ] Link to cluster synthesis
"""

    # Write file
    file_path = OUTPUT_DIR / f"{qid}.md"
    if file_path.exists() and not OVERWRITE:
        print(f"⏭️  Exists, not overwriting: {file_path}")
        continue

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(yaml_block + md_body)
        
    print(f"✅ Created: {file_path}")

print("\n🎉 All question notes generated!")
print(f"📁 Output directory: {OUTPUT_DIR.resolve()}")
print("\n🔄 Next steps:")
print("1. Open files in notes/questions/ and fill NotebookLM answers")
print("2. Use Qwen in VS Code to draft 'Distilled note' sections")
print("3. Later: merge/link these into per-paper notes or cluster syntheses")
