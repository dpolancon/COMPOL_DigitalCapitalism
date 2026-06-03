import pandas as pd
import json
import sys

def parse_registry():
    excel_path = "02_LitRev_Sistematica/land_rent_financialization_literature_registry.xlsx"
    
    try:
        # Read relevant sheets
        papers_df = pd.read_excel(excel_path, sheet_name="01_Paper_Registry")
        questions_df = pd.read_excel(excel_path, sheet_name="02_PerPaper_Questions")
        clusters_df = pd.read_excel(excel_path, sheet_name="03_Clusters")
        
        # Create lookup dictionaries
        papers = {}
        for _, row in papers_df.iterrows():
            sid = row.get("Source ID")
            if pd.notna(sid):
                papers[str(sid)] = row.to_dict()
                
        clusters = {}
        for _, row in clusters_df.iterrows():
            cid = row.get("Cluster ID")
            if pd.notna(cid):
                clusters[str(cid)] = row.to_dict()
        
        # Process questions
        questions = []
        for _, q_row in questions_df.iterrows():
            q_id = q_row.get("Question ID")
            if pd.isna(q_id) or not str(q_id).startswith("PDF"):
                continue
                
            source_id = str(q_row.get("Source ID"))
            cluster_id_raw = q_row.get("Cluster ID") # Might be in questions sheet or inferred from paper
            # Actually, let's check if Cluster ID is in questions sheet. If not, get from paper.
            # The column list for 02_PerPaper_Questions didn't show Cluster ID.
            # So we get it from the paper.
            
            paper_info = papers.get(source_id, {})
            cluster_id = str(paper_info.get("Cluster ID", "Unknown"))
            cluster_info = clusters.get(cluster_id, {})
            
            questions.append({
                "question_id": str(q_id),
                "source_id": source_id,
                "cluster_id": cluster_id,
                "question_text": q_row.get("NotebookLM question"),
                "tag": q_row.get("Question tag"),
                "status": q_row.get("Status"),
                "paper_title": paper_info.get("Title"),
                "authors": paper_info.get("Authors"),
                "year": paper_info.get("Year"),
                "venue": paper_info.get("Publication venue / status"),
                "cluster_name": cluster_info.get("Cluster name")
            })
            
        # Sort by question_id
        questions.sort(key=lambda x: x["question_id"])
        
        output = {
            "metadata": {
                "total_papers": len(papers),
                "total_questions": len(questions),
                "total_clusters": len(clusters)
            },
            "questions": questions
        }
        
        with open("02_LitRev_Sistematica/config/registry_parsed.json", "w", encoding="utf-8") as f:
            json.dump(output, f, indent=2, ensure_ascii=False)
            
        print(f"Successfully parsed {len(questions)} questions.")
        print("Output saved to 02_LitRev_Sistematica/config/registry_parsed.json")
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    parse_registry()