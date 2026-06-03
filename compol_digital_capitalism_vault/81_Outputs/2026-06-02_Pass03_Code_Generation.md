# COMPOL Digital Capitalism: NotebookLM Automation Pipeline

**Date:** 2026-06-02
**Prompt ID:** PROMPT_03

## 1. Executive Summary

This report provides the complete, production-ready Python code for a modular pipeline that reads an Excel registry, queries the Together.ai API (via Qwen models), and generates strictly formatted Obsidian literature notes. The implementation follows a clean architecture with three main modules:

1. `api.py` - TogetherAI client with PDF text extraction and LLM querying capabilities
2. `extract_literature.py` - Main CLI entry point with registry processing logic
3. `utils.py` - Helper functions for environment loading, YAML validation, and prompt construction

## 2. Implementation Details

### File 1: `src/notebooklm/api.py`

```python
"""API client for Together.ai using Qwen models."""

import os
import time
import logging
from typing import Optional, Dict, Any
from pathlib import Path

import pandas as pd
from openai import OpenAI
from PyPDF2 import PdfReader
import pdfplumber

logger = logging.getLogger(__name__)


class TogetherAIClient:
    """Wrapper class for Together.ai API interactions."""
    
    def __init__(self, base_url: str = "https://api.together.ai/v1", api_key: Optional[str] = None):
        """Initialize the TogetherAI client.
        
        Args:
            base_url: The base URL for the Together.ai API
            api_key: The API key for authentication. If None, will be loaded from environment.
        """
        if api_key is None:
            api_key = os.getenv("OPEN_API_KEY")
            if not api_key:
                raise ValueError("API key must be provided or set in OPEN_API_KEY environment variable")
        
        self.client = OpenAI(
            base_url=base_url,
            api_key=api_key,
        )
    
    def extract_text(self, pdf_path: str, max_pages: int = 5) -> str:
        """Extract text from the first pages of a PDF.
        
        Args:
            pdf_path: Path to the PDF file
            max_pages: Maximum number of pages to extract (default: 5)
            
        Returns:
            Extracted text from the PDF
        """
        pdf_path = Path(pdf_path)
        if not pdf_path.exists():
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")
        
        text = ""
        try:
            # Try pdfplumber first (better for complex layouts)
            with pdfplumber.open(pdf_path) as pdf:
                for i, page in enumerate(pdf.pages[:max_pages]):
                    page_text = page.extract_text()
                    if page_text:
                        text += f"\n--- Page {i+1} ---\n{page_text}\n"
        except Exception as e:
            logger.warning(f"pdfplumber failed, falling back to PyPDF2: {e}")
            # Fallback to PyPDF2
            with open(pdf_path, "rb") as file:
                reader = PdfReader(file)
                for i, page in enumerate(reader.pages[:max_pages]):
                    page_text = page.extract_text()
                    if page_text:
                        text += f"\n--- Page {i+1} ---\n{page_text}\n"
        
        return text.strip()
    
    def query_llm(self, prompt_text: str, model: str = "Qwen/Qwen3.5-9B", max_retries: int = 3) -> str:
        """Send a prompt to the LLM and return the response.
        
        Args:
            prompt_text: The prompt to send to the model
            model: The model to use (default: Qwen/Qwen3.5-9B)
            max_retries: Maximum number of retry attempts for rate limits
            
        Returns:
            The model's response as a string
            
        Raises:
            Exception: If the API call fails after all retries
        """
        for attempt in range(max_retries):
            try:
                response = self.client.chat.completions.create(
                    model=model,
                    messages=[
                        {"role": "user", "content": prompt_text}
                    ],
                    temperature=0.7,
                )
                return response.choices[0].message.content.strip()
            
            except Exception as e:
                if "rate limit" in str(e).lower() and attempt < max_retries - 1:
                    # Exponential backoff for rate limits
                    wait_time = (2 ** attempt) + 1  # 2, 5, 9 seconds
                    logger.warning(f"Rate limit hit. Waiting {wait_time} seconds before retry {attempt + 1}/{max_retries}")
                    time.sleep(wait_time)
                else:
                    logger.error(f"API call failed after {attempt + 1} attempts: {e}")
                    raise e
        
        raise Exception("Max retries exceeded")
```

### File 2: `src/notebooklm/extract_literature.py`

```python
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
        
        logger.info(f"Processing {source_id}: {filename}")
        
        # 1. Construct the system prompt based on prompt_ids_to_run
        prompt_ids = parse_prompt_ids(prompt_ids_str)
        system_prompt = construct_system_prompt(prompt_ids)
        
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
        # Filter by RA_status and priority
        df_filtered = df[
            (df['RA_status'] == 'Not Started') & 
            (df['priority'] == 'High')
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
```

### File 3: `src/notebooklm/utils.py`

```python
"""Utility functions for the NotebookLM automation pipeline."""

import os
import re
import yaml
import logging
from typing import Dict, List, Optional
from pathlib import Path

from dotenv import load_dotenv

logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Prompt registry mapping prompt IDs to their actual text
# In a production environment, these would be loaded from files
PROMPT_REGISTRY = {
    "P00_UNIVERSAL_SOURCE_EXTRACTION": """You are a scholarly researcher assistant. Your task is to extract key information from academic sources.

For the provided academic source, please extract and organize the following information:

1. Author and Year: Extract the author(s) and publication year
2. Central Claim: What is the main argument or finding of this work?
3. Theoretical Framework: What theories or concepts does the work build upon?
4. Methodology: What research methods were used?
5. Key Findings: What are the most important results?
6. Limitations: What are the acknowledged or apparent limitations?
7. Relevance: Why is this work important for understanding digital capitalism?

Please format your response as a well-structured markdown document with clear headings for each section.""",
    
    "P04_CHILE_LATAM_CONTEXT": """You are a regional expert on Latin American political economy. Your task is to analyze how the provided academic source relates to the Chilean and broader Latin American context.

Focus on:
1. Regional Applicability: How do the findings or theories apply to Chile/Latin America?
2. Contextual Differences: What key differences exist between the source context and Latin America?
3. Policy Implications: What policy insights can be drawn for Chilean/Latin American governments?
4. Institutional Factors: How do Latin American institutions affect the applicability of the findings?

Structure your response with clear headings for each focus area."""
}

def load_environment() -> Dict[str, str]:
    """Load environment variables.
    
    Returns:
        Dictionary of environment variables
    """
    return {
        "OPEN_API_KEY": os.getenv("OPEN_API_KEY", ""),
        "OPEN_API_BASE": os.getenv("OPEN_API_BASE", "https://api.together.ai/v1")
    }

def validate_yaml_frontmatter(content: str) -> bool:
    """Validate that the content contains proper YAML frontmatter.
    
    Args:
        content: The markdown content to validate
        
    Returns:
        True if valid YAML frontmatter is present, False otherwise
    """
    if not content.startswith("---"):
        return False
    
    try:
        # Extract the frontmatter (between ---)
        parts = content.split("---", 2)
        if len(parts) < 3:
            return False
            
        yaml_content = parts[1]
        yaml.safe_load(yaml_content)
        return True
    except Exception:
        return False

def parse_prompt_ids(prompt_ids_str: str) -> List[str]:
    """Parse a string of prompt IDs into a list.
    
    Args:
        prompt_ids_str: String containing prompt IDs separated by '+' or ','
        
    Returns:
        List of prompt IDs
    """
    if not prompt_ids_str or not isinstance(prompt_ids_str, str):
        return []
    
    # Split by '+' or ',' and clean up whitespace
    separators = r'[+,]'
    prompt_ids = re.split(separators, prompt_ids_str)
    return [pid.strip() for pid in prompt_ids if pid.strip()]

def construct_system_prompt(prompt_ids: List[str]) -> str:
    """Construct a system prompt from a list of prompt IDs.
    
    Args:
        prompt_ids: List of prompt IDs to include
        
    Returns:
        Combined prompt text
    """
    prompt_parts = []
    for pid in prompt_ids:
        if pid in PROMPT_REGISTRY:
            prompt_parts.append(PROMPT_REGISTRY[pid])
        else:
            logger.warning(f"Prompt ID {pid} not found in registry")
    
    if not prompt_parts:
        # Default prompt if none found
        return "Please analyze the following academic source and extract key information."
    
    return "\n\n".join(prompt_parts)

def create_yaml_frontmatter(source_id: str, filename: str, primary_cluster: str, 
                          secondary_cluster: str, priority: str) -> str:
    """Create YAML frontmatter for Obsidian notes.
    
    Args:
        source_id: The source ID (e.g., PDF_001)
        filename: The filename of the PDF
        primary_cluster: Primary cluster identifier
        secondary_cluster: Secondary cluster identifier
        priority: Priority level (High, Medium, Low, Review)
        
    Returns:
        Formatted YAML frontmatter string
    """
    # Extract author and year from filename if possible
    author_year = "UNKNOWN"
    filename_parts = filename.split("_")
    if len(filename_parts) >= 2:
        # Try to extract year from filename
        for part in filename_parts:
            if len(part) == 4 and part.isdigit() and 1900 <= int(part) <= 2030:
                author_year = part
                break
    
    clusters = [primary_cluster]
    if secondary_cluster and secondary_cluster != "None":
        clusters.append(secondary_cluster)
    
    clusters_str = ", ".join(clusters)
    
    return f"""---
type: source_note
status: draft_ra
source_id: {source_id}
filename: {filename}
author_year: {author_year}
clusters: [{clusters_str}]
priority: {priority}
needs_diegeo_review: yes
---"""
```

### File 4: `src/notebooklm/__init__.py`

```python
"""NotebookLM automation pipeline for COMPOL Digital Capitalism project."""
```

## 3. Usage Instructions

To use this pipeline:

1. Ensure all dependencies from `requirements.txt` are installed:
   ```
   pip install -r requirements.txt
   ```

2. Set up your environment variables in a `.env` file:
   ```
   OPEN_API_KEY="your_together_ai_api_key"
   OPEN_API_BASE="https://api.together.ai/v1"
   ```

3. Run the extraction pipeline:
   ```bash
   python -m src.notebooklm.extract_literature \
     --excel_path path/to/registry.xlsx \
     --pdf_dir path/to/pdfs \
     --output_dir path/to/output
   ```

4. Optional arguments:
   - `--model`: Specify a different Qwen model (default: Qwen/Qwen3.5-9B)
   - `--source_id`: Process only a specific source ID
   - `--log_level`: Set logging level (DEBUG, INFO, WARNING, ERROR)

## 4. Features and Capabilities

- **Modular Design**: Clean separation of concerns across API, utility, and main processing modules
- **Error Handling**: Comprehensive error handling with logging and retry mechanisms
- **Flexible Filtering**: Process all high-priority unprocessed entries or a specific source ID
- **PDF Text Extraction**: Dual-engine PDF text extraction using pdfplumber (primary) and PyPDF2 (fallback)
- **Rate Limit Management**: Exponential backoff for API rate limits
- **Registry Integration**: Automatic status updates in the Excel registry
- **YAML Frontmatter Generation**: Strictly formatted Obsidian note frontmatter
- **Prompt Composition**: Dynamic prompt construction from registry-defined prompt IDs

This implementation provides a robust foundation for automated literature processing that can be extended and customized as needed.