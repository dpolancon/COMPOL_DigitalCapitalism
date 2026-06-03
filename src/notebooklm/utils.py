"""Utility functions for the NotebookLM + Together.ai automation pipeline."""
import os
import re
import yaml
import logging
import pandas as pd
from typing import Dict, List, Optional
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

# Hardcoded fallback prompt registry
PROMPT_REGISTRY_FALLBACK = {
    "P00_UNIVERSAL_SOURCE_EXTRACTION": """Extract bibliographic identity, what the source studies, method and corpus, core claims, relevance to Diego's paper, cluster tags, possible citation uses, limits, open questions.""",
    "P01_PAID_ADS_OBJECT": """Extract whether source studies paid ads or organic posts, platform, targeting mechanism, ad visibility, disclosure, persuasion, segmentation, audience control.""",
    "P02_TOPIC_MODELING_METHOD": """Extract method type (LDA/STM/BERTopic/etc.), corpus, validation strategy, preprocessing choices, Spanish/short-text/political-ad text handling, method limitations, how to cite.""",
    "P03_PLATFORMIZATION_DIGITAL_POLITICS": """Extract concept of digitalization/platformization/datafication, actors, platform framing (channel vs. infrastructure), geographic scope, mechanisms linking platforms to campaign strategy, Chile 2021 bridge sentence.""",
    "P04_CHILE_LATAM_CONTEXT": """Extract country/election studied, Chile 2019 uprising / constitutional process / party fragmentation / candidate references, LatAm distinctiveness, platforms used, contrast case for Chile 2021, justification sentence for Chile as theoretical case.""",
    "P05_ETHICS_MANIPULATION_RISK": """Extract risks named (manipulation/privacy/polarization/etc.), empirical evidence vs. speculation, whether microtargeting is inherently harmful or over-feared, platform/campaign/regulator roles, counterargument, ethics/evidence debate framing sentence.""",
    "P06_DIGITAL_CAPITALISM_PLATFORM_POWER": """Extract theoretical object (platform capitalism/digital labor/data extraction/etc.), power mechanism, how source theorizes political advertising as platform-mediated infrastructure, portable concepts, what to exclude, 3 conceptual building blocks.""",
    "P07_VENUE_PRECEDENT": """Extract journal, year, article type, niche coverage (method/object/region/case/theory/platform/venue), relationship to Diego's paper (competitor/analogue/precedent/background), gap remaining after this source, one-sentence citation use.""",
    "P08_CHATGPT_NORMALIZE_TO_OBSIDIAN": """Convert the following NotebookLM output into an Obsidian source note. Do not add claims not present in the output. Use this structure:

---
type: source_note
status: draft_ra
source_id: [INSERT SOURCE ID]
filename: [INSERT FILENAME]
author_year: [EXTRACT FROM TEXT]
clusters: [INSERT CLUSTERS]
priority: [INSERT PRIORITY]
needs_diego_review: yes
---

# [AUTHOR YEAR] — [Short Title]

## Bibliographic identity
## What this source studies
## Method and corpus
## Core claims / findings
## Relevance to Diego paper
## Cluster tags
## Possible citation uses
## Limits / do not infer
## Open questions for checkpoint

Now normalize this NotebookLM output:"""
}

def load_prompt_registry(excel_path: str) -> Dict[str, str]:
    """Dynamically load the Prompt_Bank sheet from the RA's Excel registry. Falls back to hardcoded prompts if not found."""
    path = Path(excel_path)
    if not path.exists():
        raise FileNotFoundError(f"Excel registry not found at: {path}")
        
    try:
        df_prompts = pd.read_excel(path, sheet_name='Prompt_Bank')
        if 'prompt_id' not in df_prompts.columns or 'prompt_text' not in df_prompts.columns:
            raise ValueError("Excel 'Prompt_Bank' sheet must contain 'prompt_id' and 'prompt_text' columns.")
            
        registry = dict(zip(df_prompts['prompt_id'], df_prompts['prompt_text']))
        registry = {k: v for k, v in registry.items() if pd.notna(k) and pd.notna(v)}
        logger.info(f"Successfully loaded {len(registry)} prompts from Excel Prompt_Bank.")
        return registry
    except Exception as e:
        logger.warning(f"Failed to load prompt registry from Excel sheet 'Prompt_Bank': {e}. Falling back to hardcoded prompt registry.")
        return PROMPT_REGISTRY_FALLBACK


def parse_prompt_ids(prompt_ids_str: str) -> List[str]:
    """Parse the 'prompt_ids_to_run' string into a clean list."""
    if not prompt_ids_str or not isinstance(prompt_ids_str, str):
        return []
    separators = r'[+,]'
    prompt_ids = re.split(separators, prompt_ids_str)
    return [pid.strip() for pid in prompt_ids if pid.strip()]

def build_extraction_prompt(prompt_ids_str: str, prompt_registry: Dict[str, str]) -> str:
    """Constructs the combined extraction prompt (P00 + PX) from the registry."""
    ids = parse_prompt_ids(prompt_ids_str)
    extraction_parts = []
    
    for pid in ids:
        if pid == "P08_CHATGPT_NORMALIZE_TO_OBSIDIAN":
            continue # Handled separately by Together.ai
            
        if pid in prompt_registry:
            extraction_parts.append(prompt_registry[pid])
        else:
            logger.warning(f"Prompt ID '{pid}' not found in the Excel Prompt_Bank registry.")
            
    if not extraction_parts:
        logger.error("No valid extraction prompts found. Falling back to generic prompt.")
        return "Please analyze the following academic source and extract key information."
        
    return "\n\n---\n\n".join(extraction_parts)

def get_p08_normalization_prompt(prompt_registry: Dict[str, str]) -> str:
    """Fetches the P08 ChatGPT Normalization prompt directly from the Excel registry."""
    p08_id = "P08_CHATGPT_NORMALIZE_TO_OBSIDIAN"
    if p08_id in prompt_registry:
        return prompt_registry[p08_id]
    
    logger.warning("P08 not found in registry. Using hardcoded fallback.")
    return """Convert the following NotebookLM output into an Obsidian source note. Do not add claims not present in the output. Use this structure:

---
type: source_note
status: draft_ra
source_id: [INSERT SOURCE ID]
filename: [INSERT FILENAME]
author_year: [EXTRACT FROM TEXT]
clusters: [INSERT CLUSTERS]
priority: [INSERT PRIORITY]
needs_diego_review: yes
---

# [AUTHOR YEAR] — [Short Title]

## Bibliographic identity
## What this source studies
## Method and corpus
## Core claims / findings
## Relevance to Diego paper
## Cluster tags
## Possible citation uses
## Limits / do not infer
## Open questions for checkpoint

Now normalize this NotebookLM output:"""

def create_yaml_frontmatter(source_id: str, filename: str, primary_cluster: str, secondary_cluster: Optional[str], priority: str) -> str:
    """Generates the strict YAML frontmatter required for the Obsidian vault."""
    author_year = "UNKNOWN"
    filename_base = Path(filename).stem
    parts = filename_base.split("_")
    
    for part in parts:
        if len(part) == 4 and part.isdigit() and 1900 <= int(part) <= 2030:
            author_year = part
            break
            
    if author_year != "UNKNOWN" and len(parts) > 1:
        author_part = parts[0]
        if len(parts) > 2 and parts[1] not in ["ETAL", "ET", "AL"]:
            author_part = f"{parts[0]} {parts[1]}"
        author_year = f"{author_part} {author_year}"

    clusters = [primary_cluster]
    if secondary_cluster and str(secondary_cluster).lower() not in ["none", "nan", ""]:
        clusters.append(str(secondary_cluster))
        
    yaml_data = {
        "type": "source_note",
        "status": "draft_ra",
        "source_id": source_id,
        "filename": filename,
        "author_year": author_year,
        "clusters": clusters,
        "priority": priority,
        "needs_diego_review": True
    }
    
    yaml_str = yaml.dump(yaml_data, default_flow_style=False, sort_keys=False, allow_unicode=True)
    return f"---\n{yaml_str}---"

def construct_system_prompt(prompt_ids: List[str]) -> str:
    """Construct a system prompt from a list of prompt IDs using fallback registry."""
    prompt_parts = []
    for pid in prompt_ids:
        if pid in PROMPT_REGISTRY_FALLBACK:
            prompt_parts.append(PROMPT_REGISTRY_FALLBACK[pid])
        else:
            logger.warning(f"Prompt ID {pid} not found in fallback registry")
    
    if not prompt_parts:
        return "Please analyze the following academic source and extract key information."
    
    return "\n\n".join(prompt_parts)

def load_environment() -> Dict[str, str]:
    """Load environment variables.
    
    Returns:
        Dictionary of environment variables
    """
    return {
        "OPEN_API_KEY": os.getenv("OPEN_API_KEY", ""),
        "OPEN_API_BASE": os.getenv("OPEN_API_BASE", "https://api.together.ai/v1")
    }