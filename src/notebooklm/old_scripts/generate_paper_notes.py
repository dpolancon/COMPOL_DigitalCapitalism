#!/usr/bin/env python3
"""
Generate Obsidian-ready markdown notes from the Land-Rent Literature Registry.
Outputs:
  - notes/papers/PDFXXX.md (one per paper)
  - notes/validation/PDFXXX_validation.json (checklist for review)
  - notes/quotes/PDFXXX_quotes.md (quote/page extraction template)
"""

import pandas as pd
import json
import os
from pathlib import Path
from datetime import datetime

# Configuration
EXCEL_PATH = "02_LitRev_Sistematica/land_rent_financialization_literature_registry.xlsx"
OUTPUT_DIR = Path("notes")
PAPERS_DIR = OUTPUT_DIR / "papers"
VALIDATION_DIR = OUTPUT_DIR / "validation"
QUOTES_DIR = OUTPUT_DIR / "quotes"

# Ensure directories exist
for d in [PAPERS_DIR, VALIDATION_DIR, QUOTES_DIR]:
    d.mkdir(parents=True, exist_ok=True)

# Load Excel sheets
xls = pd.ExcelFile(EXCEL_PATH)
paper_registry = pd.read_excel(xls, sheet_name="01_Paper_Registry")
per_paper_qs = pd.read_excel(xls, sheet_name="02_PerPaper_Questions")
obsidian_template = pd.read_excel(xls, sheet_name="06_Obsidian_Template")

def generate_yaml_frontmatter(row, cluster_info=None):
    """Generate YAML frontmatter for Obsidian"""
    return f"""---
source_id: {row['Source ID']}
filename: {row['Filename']}
citation_key: {row['Citation key']}
authors: {row['Authors']}
year: {int(row['Year']) if pd.notna(row['Year']) else ''}
title: {row['Title']}
cluster: {row['Cluster ID']}
priority: {row['Priority']}
status: not_started
created: {datetime.now().strftime('%Y-%m-%d')}
updated: {datetime.now().strftime('%Y-%m-%d')}
tags: [land-rent, financialization, {row['Cluster ID']}]
---
"""

def get_questions_for_paper(source_id, questions_df):
    """Extract all questions for a given paper"""
    paper_qs = questions_df[questions_df['Source ID'] == source_id].copy()
    return paper_qs.to_dict('records') if not paper_qs.empty else []

def generate_note_content(row, questions, template_df):
    """Generate the full markdown note content"""
    yaml = generate_yaml_frontmatter(row)
    
    # Get template instructions
    template_rows = template_df.to_dict('records')
    
    content = [yaml, ""]
    
    # Central claim (placeholder)
    content.append("## 1. Central Claim")
    content.append("*[To be filled after NotebookLM query]*")
    content.append("")
    
    # Model object
    content.append("## 2. Model Object")
    content.append(f"- **Core object**: {row['Core object']}")
    content.append(f"- **Main mechanism**: {row['Main mechanism']}")
    content.append(f"- **Project role**: {row['Project role']}")
    content.append("")
    
    # Mechanism section with questions
    content.append("## 3. Mechanism (NotebookLM Extraction)")
    content.append("*Answers to per-paper questions:*")
    content.append("")
    
    for i, q in enumerate(questions, 1):
        content.append(f"### {q['Question ID']}: {q['NotebookLM question']}")
        content.append(f"*Tag: {q['Question tag']} | Status: {q['Status']}*")
        content.append("")
        content.append("> *[NotebookLM answer goes here]*")
        content.append("")
        content.append("**Distilled note for Obsidian:**")
        content.append("*[Your paraphrase here]*")
        content.append("")
    
    # Formal result
    content.append("## 4. Formal Result (if applicable)")
    content.append("*[Theorem/proposition with assumptions and intuition]*")
    content.append("")
    
    # Evidence
    content.append("## 5. Evidence / Motivation")
    content.append("*[Figures, stylized facts, empirical references]*")
    content.append("")
    
    # Project translation
    content.append("## 6. Project Translation")
    content.append(f"*How this helps the Fondecyt land-rent / financialization branch:*")
    content.append("")
    
    # Critique
    content.append("## 7. Critique / Limits")
    content.append("*[Assumptions that may not hold for Latin American contexts]*")
    content.append("")
    
    # Quotable paraphrase
    content.append("## 8. Quotable Paraphrase")
    content.append("*[Clean paraphrase with page marker, no long quotes]*")
    content.append("")
    
    # Source link
    if pd.notna(row['Source URL']):
        content.append(f"## 🔗 Source")
        content.append(f"[View PDF]({row['Source URL']})")
        content.append("")
    
    return "\n".join(content)

def generate_validation_checklist(row, questions):
    """Generate JSON validation checklist"""
    return {
        "source_id": row['Source ID'],
        "validation_date": None,
        "validated_by": None,
        "checks": [
            {
                "field": "central_claim",
                "description": "Is the central claim accurately summarized in 1-2 sentences?",
                "status": "pending",
                "notes": ""
            },
            {
                "field": "mechanism_extraction",
                "description": "Are all per-paper questions answered with NotebookLM?",
                "status": "pending",
                "notes": ""
            },
            {
                "field": "formal_result",
                "description": "Is the formal result (if any) correctly stated with assumptions?",
                "status": "pending",
                "notes": ""
            },
            {
                "field": "project_translation",
                "description": "Does the note clearly connect to the Fondecyt project questions?",
                "status": "pending",
                "notes": ""
            },
            {
                "field": "critique",
                "description": "Are limitations for Latin American application identified?",
                "status": "pending",
                "notes": ""
            }
        ],
        "quotes_to_verify": [
            {
                "question_id": q['Question ID'],
                "notebooklm_answer": None,
                "source_page": None,
                "quote_text": None,
                "verified_in_chatgpt": False,
                "verified_in_gemini": False
            }
            for q in questions
        ]
    }

def generate_quotes_template(row, questions):
    """Generate markdown template for quote extraction"""
    content = [
        f"# Quote Extraction: {row['Source ID']}",
        f"**Paper**: {row['Title']}",
        f"**Cluster**: {row['Cluster ID']}",
        "",
        "## Instructions",
        "1. Run each question in NotebookLM with the source loaded",
        "2. Copy the answer + page reference",
        "3. Paste below under the corresponding question",
        "4. Validate key quotes in ChatGPT/Gemini project chat",
        "",
        "---",
        ""
    ]
    
    for q in questions:
        content.append(f"### {q['Question ID']}")
        content.append(f"**Question**: {q['Question ID']}: {q['NotebookLM question']}")
        content.append("")
        content.append("```notebooklm")
        content.append("# Paste NotebookLM answer here")
        content.append("# Include page numbers if available")
        content.append("```")
        content.append("")
        content.append("✅ Validated in ChatGPT project: [ ]")
        content.append("✅ Validated in Gemini/NotebookLM: [ ]")
        content.append("")
        content.append("---")
        content.append("")
    
    return "\n".join(content)

def main():
    print(f"📊 Reading registry from {EXCEL_PATH}...")
    
    for _, row in paper_registry.iterrows():
        source_id = row['Source ID']
        print(f"📄 Processing {source_id}: {row['Title'][:50]}...")
        
        # Get questions for this paper
        questions = get_questions_for_paper(source_id, per_paper_qs)
        
        # Generate note
        note_content = generate_note_content(row, questions, obsidian_template)
        note_path = PAPERS_DIR / f"{source_id}.md"
        with open(note_path, 'w', encoding='utf-8') as f:
            f.write(note_content)
        print(f"   ✓ Created {note_path}")
        
        # Generate validation checklist
        validation = generate_validation_checklist(row, questions)
        validation_path = VALIDATION_DIR / f"{source_id}_validation.json"
        with open(validation_path, 'w', encoding='utf-8') as f:
            json.dump(validation, f, indent=2, ensure_ascii=False)
        print(f"   ✓ Created validation checklist: {validation_path}")
        
        # Generate quotes template
        quotes_content = generate_quotes_template(row, questions)
        quotes_path = QUOTES_DIR / f"{source_id}_quotes.md"
        with open(quotes_path, 'w', encoding='utf-8') as f:
            f.write(quotes_content)
        print(f"   ✓ Created quotes template: {quotes_path}")
        
        print("")
    
    print("✅ All notes generated!")
    print(f"📁 Output directory: {OUTPUT_DIR.resolve()}")
    print("\n🔄 Next steps:")
    print("1. Import papers into NotebookLM by cluster")
    print("2. Run per-paper questions and paste answers into notes/")
    print("3. Use validation/ files to review each note")
    print("4. Use quotes/ files to extract & verify key passages")

if __name__ == "__main__":
    main()