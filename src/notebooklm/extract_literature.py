"""Main CLI entry point for extracting literature notes using LLMs."""

import argparse
import logging
import pandas as pd
from pathlib import Path
from typing import Optional

from .api import TogetherAIClient
from .utils import (
    parse_prompt_ids, 
    construct_system_prompt, 
    create_yaml_frontmatter,
    load_environment
)

logger = logging.getLogger(__name__)

def update_registry_status(excel_path: str, source_id: str, new_status: str = "Processed_Pending_Review") -> None:
    """Update the RA_status for a specific source_id in the Excel registry.
    
    Args:
        excel_path: Path to the Excel registry file
        source_id: The source_id to update
        new_status: The new status to set
    """
    try:
        # Load the Excel file
        df = pd.read_excel(excel_path)
        
        # Update the status for the specific source_id
        mask = df['source_id'] == source_id
        if mask.any():
            df.loc[mask, 'RA_status'] = new_status
            
            # Save back to Excel
            df.to_excel(excel_path, index=False)
            logger.info(f"Updated status for {source_id} to {new_status}")
        else:
            logger.warning(f"Source ID {source_id} not found in registry")
    except Exception as e:
        logger.error(f"Failed to update registry status for {source_id}: {e}")

def process_single_source(
    client: TogetherAIClient,
    row: pd.Series,
    pdf_dir: str,
    output_dir: str,
    model: str = "Qwen/Qwen3.5-9B"
) -> bool:
    """Process a single source row from the registry.
    
    Args:
        client: The TogetherAI client
        row: A pandas Series representing a row from the registry
        pdf_dir: Directory containing PDF files
        output_dir: Directory to save output files
        model: The model to use for processing
        
    Returns:
        True if processing was successful, False otherwise
    """
    try:
        source_id = row['source_id']
        filename = row['filename']
        relative_path = row['relative_path']
        primary_cluster = row['primary_cluster']
        secondary_cluster = row.get('secondary_cluster', '')
        priority = row['priority']
        prompt_ids_str = row['prompt_ids_to_run']
        output_filename = row['output_obsidian_note']
        paper_specific_questions = row.get('paper_specific_questions', '')
        
        logger.info(f"Processing {source_id}: {filename}")
        
        # 1. Construct the system prompt based on prompt_ids_to_run
        prompt_ids = parse_prompt_ids(prompt_ids_str)
        system_prompt = construct_system_prompt(prompt_ids)
        
        # Append paper-specific questions to system prompt if present
        if pd.notna(paper_specific_questions) and str(paper_specific_questions).strip():
            system_prompt = f"{system_prompt}\n\n---\n\nPAPER-SPECIFIC QUESTIONS TO ANSWER:\n{paper_specific_questions}"
        
        # 2. Extract text from the PDF
        pdf_path = Path(pdf_dir) / relative_path
        if not pdf_path.exists():
            logger.error(f"PDF file not found: {pdf_path}")
            return False
            
        pdf_text = client.extract_text(str(pdf_path))
        if not pdf_text:
            logger.error(f"No text extracted from PDF: {pdf_path}")
            return False
        
        # 3. Combine the system prompt and the PDF text
        full_prompt = f"{system_prompt}\n\nPlease analyze the following academic source:\n\n{pdf_text}"
        
        # 4. Call the LLM
        llm_response = client.query_llm(full_prompt, model=model)
        
        # 5. Create YAML frontmatter
        yaml_frontmatter = create_yaml_frontmatter(
            source_id, filename, primary_cluster, secondary_cluster, priority
        )
        
        # 6. Combine frontmatter with LLM response
        full_output = f"{yaml_frontmatter}\n\n{llm_response}"
        
        # 7. Save the output as a .md file
        output_path = Path(output_dir) / output_filename
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(full_output)
        
        logger.info(f"Saved output to {output_path}")
        return True
        
    except Exception as e:
        logger.error(f"Error processing {source_id}: {e}")
        return False

def main():
    """Main entry point for the literature extraction pipeline."""
    parser = argparse.ArgumentParser(description="Extract literature notes using LLMs")
    parser.add_argument("--excel_path", required=True, help="Path to the Excel registry file")
    parser.add_argument("--pdf_dir", required=True, help="Directory containing PDF files")
    parser.add_argument("--output_dir", required=True, help="Directory to save output files")
    parser.add_argument("--model", default="Qwen/Qwen3.5-9B", help="Model to use for processing")
    parser.add_argument("--source_id", help="Process only a specific source_id")
    parser.add_argument("--log_level", default="INFO", help="Logging level (DEBUG, INFO, WARNING, ERROR)")
    
    args = parser.parse_args()
    
    # Set up logging
    logging.basicConfig(
        level=getattr(logging, args.log_level.upper(), logging.INFO),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Load environment variables
    env_vars = load_environment()
    
    # Initialize the TogetherAI client
    client = TogetherAIClient(
        base_url=env_vars["OPEN_API_BASE"],
        api_key=env_vars["OPEN_API_KEY"]
    )
    
    # Load the Excel registry
    try:
        df = pd.read_excel(args.excel_path)
        logger.info(f"Loaded registry with {len(df)} entries")
    except Exception as e:
        logger.error(f"Failed to load Excel registry: {e}")
        return
    
    # Filter rows
    if args.source_id:
        # Process only the specified source_id
        df_filtered = df[df['source_id'] == args.source_id]
        if df_filtered.empty:
            logger.error(f"Source ID {args.source_id} not found in registry")
            return
    else:
        # Filter all remaining unprocessed sources (High/Medium/Low priority)
        df_filtered = df[
            (df['RA_status'] == 'Not Started') & 
            (df['primary_cluster'] != 'AUX_METADATA_OR_FRONTMATTER')
        ]
    
    if df_filtered.empty:
        logger.info("No entries to process")
        return
    
    logger.info(f"Processing {len(df_filtered)} entries")
    
    # Process each row
    processed_count = 0
    success_count = 0
    
    for _, row in df_filtered.iterrows():
        processed_count += 1
        source_id = row['source_id']
        
        logger.info(f"Processing {processed_count}/{len(df_filtered)}: {source_id}")
        
        success = process_single_source(
            client, row, args.pdf_dir, args.output_dir, args.model
        )
        
        if success:
            success_count += 1
            # Update the registry status
            update_registry_status(args.excel_path, source_id)
        else:
            logger.error(f"Failed to process {source_id}")
    
    logger.info(f"Processing complete: {success_count}/{processed_count} successful")

if __name__ == "__main__":
    main()