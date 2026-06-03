"""Hybrid pipeline: NotebookLM for extraction, Together.ai for Obsidian normalization."""
import argparse
import logging
import pandas as pd
from pathlib import Path

from .notebooklm_cli import NotebookLM_CLI
from .api import TogetherAIClient
from .utils import load_prompt_registry, build_extraction_prompt, get_p08_normalization_prompt

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def process_single_pdf_hybrid(nlm: NotebookLM_CLI, together: TogetherAIClient, pdf_path: str, extraction_prompt: str, p08_prompt: str, source_id: str) -> str:
    """Orchestrates the hybrid extraction and normalization pipeline."""
    logger.info(f"[{source_id}] Creating temporary NotebookLM notebook...")
    nb_id = nlm.create_notebook(f"Temp_Extract_{source_id}")
    
    try:
        logger.info(f"[{source_id}] Uploading PDF to NotebookLM...")
        nlm.add_source_and_wait(nb_id, pdf_path)
        
        logger.info(f"[{source_id}] Querying NotebookLM with P00+PX prompts...")
        raw_extraction = nlm.ask(nb_id, extraction_prompt)
        
        if not raw_extraction or len(raw_extraction.strip()) < 50:
            raise ValueError("NotebookLM returned an empty or insufficient answer.")
            
    finally:
        logger.info(f"[{source_id}] Cleaning up temporary NotebookLM notebook...")
        try:
            nlm.delete_notebook(nb_id)
        except Exception as cleanup_err:
            logger.warning(f"Failed to delete temp notebook {nb_id}: {cleanup_err}")

    logger.info(f"[{source_id}] Normalizing raw extraction via Qwen (P08)...")
    p08_full_prompt = f"{p08_prompt}\n\n---\n\nNOTEBOOKLM OUTPUT TO NORMALIZE:\n{raw_extraction}"
    
    formatted_obsidian_note = together.query_llm(
        p08_full_prompt, 
        model="Qwen/Qwen3.5-9B",
        max_retries=3
    )
    
    return formatted_obsidian_note

def main():
    parser = argparse.ArgumentParser(description="Hybrid NotebookLM + Together.ai Literature Pipeline")
    parser.add_argument("--excel_path", required=True, help="Path to RA_NotebookLM_Obsidian_Registry.xlsx")
    parser.add_argument("--pdf_dir", required=True, help="Root directory containing the PDFs")
    parser.add_argument("--output_dir", required=True, help="Obsidian vault literature directory")
    parser.add_argument("--model", default="Qwen/Qwen3.5-9B", help="Together.ai model for P08 normalization")
    parser.add_argument("--source_id", help="Process only a specific source_id (e.g., PDF_059)")
    args = parser.parse_args()

    nlm = NotebookLM_CLI()
    together = TogetherAIClient()
    
    prompt_registry = load_prompt_registry(args.excel_path)
    p08_prompt = get_p08_normalization_prompt(prompt_registry)
    
    df_registry = pd.read_excel(args.excel_path, sheet_name='Registry')
    
    if args.source_id:
        df_process = df_registry[df_registry['source_id'] == args.source_id]
    else:
        df_process = df_registry[
            (df_registry['RA_status'] == 'Not Started') & 
            (df_registry['checkpoint_flag'] == 'GREEN') &
            (df_registry['primary_cluster'] != 'AUX_METADATA_OR_FRONTMATTER')
        ]

    if df_process.empty:
        logger.info("No eligible rows found to process.")
        return

    logger.info(f"Starting hybrid extraction for {len(df_process)} sources...")

    for _, row in df_process.iterrows():
        source_id = row['source_id']
        filename = row['filename']
        rel_path = row['relative_path']
        output_note = row['output_obsidian_note']
        prompt_ids_str = row['prompt_ids_to_run']
        
        logger.info(f"=== Processing {source_id}: {filename} ===")
        
        pdf_path = Path(args.pdf_dir) / rel_path
        if not pdf_path.exists():
            pdf_path = Path(args.pdf_dir) / filename 
            
        if not pdf_path.exists():
            logger.error(f"PDF not found at {pdf_path}. Skipping.")
            continue
            
        try:
            extraction_prompt = build_extraction_prompt(prompt_ids_str, prompt_registry)
            paper_specific_questions = row.get('paper_specific_questions', '')
            if pd.notna(paper_specific_questions) and str(paper_specific_questions).strip():
                extraction_prompt = f"{extraction_prompt}\n\n---\n\nPAPER-SPECIFIC QUESTIONS TO ANSWER:\n{paper_specific_questions}"
            
            final_markdown = process_single_pdf_hybrid(
                nlm, together, str(pdf_path), extraction_prompt, p08_prompt, source_id
            )
            
            out_path = Path(args.output_dir) / output_note
            out_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(final_markdown)
            logger.info(f"Successfully saved note to {out_path}")
            
            df_registry.loc[df_registry['source_id'] == source_id, 'RA_status'] = 'Saved in Obsidian'
            df_registry.to_excel(args.excel_path, sheet_name='Registry', index=False)
            logger.info(f"Updated Excel registry status for {source_id} to 'Saved in Obsidian'")
            
        except Exception as e:
            logger.error(f"Failed to process {source_id}: {e}")

if __name__ == "__main__":
    main()