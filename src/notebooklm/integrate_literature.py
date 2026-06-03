"""Literature review integration script.

This script synthesizes 66 paper notes into 7 cluster notes and 6 conceptual framework notes.
It uses Together.ai's Moonshot Kimi-K2.6 model.
"""

import os
import re
import yaml
import logging
import argparse
import pandas as pd
from pathlib import Path
from typing import Dict, List, Tuple, Any

from .api import TogetherAIClient
from .utils import load_environment

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

CLUSTER_DEFINITIONS = {
    "G1_PAID_ADS_OBJECT": "Studies paid digital advertising campaigns, platform architectures, targeting mechanisms, visibility, disclosure, and audience control.",
    "G2_TOPIC_MODELING_METHOD": "Focuses on computational text-as-data methods, specifically topic modeling (LDA, STM, BERTopic), preprocessing choices, short-text handling, Spanish language compatibility, and validation strategies.",
    "G3_PLATFORMIZATION_DIGITAL_POLITICS": "Explores the digitalization, platformization, and datafication of political communication, viewing platforms as campaign infrastructures rather than passive channels.",
    "G4_CHILE_LATAM_CASE_CONTEXT": "Investigates the Latin American and Chilean context, including elections, post-2019 uprising dynamics, constitutional processes, and regional campaigning distinctiveness.",
    "G5_ETHICS_MANIPULATION_RISK": "Analyzes democratic risk factors such as manipulation, polarization, privacy issues, misinformation, and unequal exposure, distinguishing empirical evidence from theoretical fear.",
    "G6_DIGITAL_CAPITALISM_PLATFORM_POWER": "Theorizes digital capitalism, platform power, data extraction, commodification of attention, and class/labor dynamics in platform-mediated politics (Fuchs' perspective).",
    "G7_VENUE_POSITIONING_PRECEDENT": "Evaluates target journals, positioning precedents, and conceptual analogues for quantitative political communication research."
}

CLUSTER_KEYS = {
    "G1_PAID_ADS_OBJECT": ("NB01_Paid_Digital_Ads", "Paid Digital Ads"),
    "G2_TOPIC_MODELING_METHOD": ("NB02_Topic_Modeling_Methods", "Topic Modeling Methods"),
    "G3_PLATFORMIZATION_DIGITAL_POLITICS": ("NB03_Platformization_Digital_Politics", "Platformization of Digital Politics"),
    "G4_CHILE_LATAM_CASE_CONTEXT": ("NB04_Chile_LatAm_Context", "Chile and Latin American Context"),
    "G5_ETHICS_MANIPULATION_RISK": ("NB05_Ethics_Manipulation_Risk", "Ethics and Manipulation Risk"),
    "G6_DIGITAL_CAPITALISM_PLATFORM_POWER": ("NB06_Digital_Capitalism_Platform_Power", "Digital Capitalism and Platform Power"),
    "G7_VENUE_POSITIONING_PRECEDENT": ("NB07_Venue_Positioning_Precedents", "Venue Positioning and Precedents")
}

CLUSTER_QUESTIONS = {
    "G1_PAID_ADS_OBJECT": "Does the source study paid ads or organic posts? What platform? What targeting mechanism? What does it say about ad visibility, disclosure, persuasion, segmentation, or audience control?",
    "G2_TOPIC_MODELING_METHOD": "What method is used? What corpus? What validation strategy? Topic number K? What preprocessing choices? Does it discuss short texts, Spanish, interpretability, or alternatives to LDA?",
    "G3_PLATFORMIZATION_DIGITAL_POLITICS": "How does the source define digitalization/platformization? What mechanisms are named? Does it treat platforms as passive channels or active infrastructures? Is the pattern global, local, or comparative?",
    "G4_CHILE_LATAM_CASE_CONTEXT": "Which country/election is studied? What makes the context distinctive? Does it discuss Chile 2021, post-2019 politics, party fragmentation, LatAm platforms, or regional campaign practices?",
    "G5_ETHICS_MANIPULATION_RISK": "What democratic risk is identified? Is the concern manipulation, privacy, polarization, misinformation, opacity, unequal exposure, or persuasion? Does the source distinguish fear from evidence?",
    "G6_DIGITAL_CAPITALISM_PLATFORM_POWER": "What theory of digital capitalism/platform power is offered? Does it explain data extraction, commodification, governance, visibility, control, or political subject formation? How could this deepen the conceptual framework?",
    "G7_VENUE_POSITIONING_PRECEDENT": "What journal published this? Why is it a precedent? Which side of the paper's niche does it cover: method, object, region, or theory? Is it a competitor, complement, or legitimating precedent?"
}

CONCEPTUAL_FRAMEWORKS = {
    "CF01_Microtargeting_As_Digital_Capitalism": {
        "title": "CF01_Microtargeting_As_Digital_Capitalism",
        "clusters": ["G1_PAID_ADS_OBJECT", "G6_DIGITAL_CAPITALISM_PLATFORM_POWER"],
        "goal": "Integrate Paid Ads (G1) and Digital Capitalism / Platform Power (G6) to conceptualize how microtargeting practices instantiate platform capitalism logic. Address how user data extraction, commodification of attention, and power asymmetries shape political campaign infrastructure.",
        "cluster_files": ["NB01_Paid_Digital_Ads", "NB06_Digital_Capitalism_Platform_Power"]
    },
    "CF02_Methodological_Approach_Topic_Modeling": {
        "title": "CF02_Methodological_Approach_Topic_Modeling",
        "clusters": ["G2_TOPIC_MODELING_METHOD", "G7_VENUE_POSITIONING_PRECEDENT"],
        "goal": "Integrate Topic Modeling Methods (G2) and Venue Precedents (G7) to argue why LDA/text-as-data is appropriate for exposing platform power dynamics and mapping political campaign communication. Validate this quantitative methodology against peer precedents.",
        "cluster_files": ["NB02_Topic_Modeling_Methods", "NB07_Venue_Positioning_Precedents"]
    },
    "CF03_Platformization_Of_Politics": {
        "title": "CF03_Platformization_Of_Politics",
        "clusters": ["G3_PLATFORMIZATION_DIGITAL_POLITICS", "G4_CHILE_LATAM_CASE_CONTEXT"],
        "goal": "Integrate Platformization of Politics (G3) and Chile / LatAm Context (G4) to explain how platformization operates differently in Latin American and Global South crisis contexts, noting media capture, high digital penetration, and structural fragmentation.",
        "cluster_files": ["NB03_Platformization_Digital_Politics", "NB04_Chile_LatAm_Context"]
    },
    "CF04_Democratic_Risk_Vs_Evidence": {
        "title": "CF04_Democratic_Risk_Vs_Evidence",
        "clusters": ["G5_ETHICS_MANIPULATION_RISK", "G4_CHILE_LATAM_CASE_CONTEXT"],
        "goal": "Integrate Ethics/Manipulation Risk (G5) and Chile / LatAm Context (G4) to distinguish dystopian fears of digital manipulation from empirically-documented political outcomes in Latin America. Use a critical political economy lens.",
        "cluster_files": ["NB05_Ethics_Manipulation_Risk", "NB04_Chile_LatAm_Context"]
    },
    "CF05_Chile_2021_As_Constitutive_Context": {
        "title": "CF05_Chile_2021_As_Constitutive_Context",
        "clusters": ["G4_CHILE_LATAM_CASE_CONTEXT", "G3_PLATFORMIZATION_DIGITAL_POLITICS", "G6_DIGITAL_CAPITALISM_PLATFORM_POWER"],
        "goal": "Integrate Chile Context (G4), Platformization (G3), and Platform Power (G6) to position the 2021 Chile presidential campaign (post-uprising, constitutional convention, pandemic) as a theoretically generative, unique case study of platform-mediated politics.",
        "cluster_files": ["NB04_Chile_LatAm_Context", "NB03_Platformization_Digital_Politics", "NB06_Digital_Capitalism_Platform_Power"]
    },
    "CF06_Integrated_Analytical_Framework": {
        "title": "CF06_Integrated_Analytical_Framework",
        "clusters": list(CLUSTER_KEYS.keys()),
        "goal": "Integrate ALL clusters (G1-G7) into a complete, unified analytical and theoretical framework connecting platform capitalism → political crisis → microtargeting strategies → democratic implications for Chile 2021.",
        "cluster_files": [val[0] for val in CLUSTER_KEYS.values()]
    }
}


def parse_yaml_frontmatter(file_path: Path) -> Dict[str, Any]:
    """Parse YAML frontmatter from a markdown file."""
    try:
        content = file_path.read_text(encoding='utf-8')
        if not content.startswith('---'):
            return {}
        parts = content.split('---', 2)
        if len(parts) >= 3:
            return yaml.safe_load(parts[1]) or {}
    except Exception as e:
        logger.error(f"Failed to parse frontmatter for {file_path.name}: {e}")
    return {}


def load_papers_metadata(papers_dir: Path) -> List[Dict[str, Any]]:
    """Load metadata and paths for all paper notes."""
    papers = []
    for f in sorted(papers_dir.glob('PDF_*.md')):
        meta = parse_yaml_frontmatter(f)
        if meta:
            papers.append({
                "file_path": f,
                "filename": f.name,
                "source_id": meta.get("source_id", f.stem.split('_')[0] + '_' + f.stem.split('_')[1]),
                "author_year": meta.get("author_year", "UNKNOWN"),
                "clusters": meta.get("clusters", []),
                "content": f.read_text(encoding='utf-8')
            })
    logger.info(f"Loaded metadata for {len(papers)} paper notes.")
    return papers


def extract_relevant_sections(note_content: str, cluster_code: str) -> str:
    """Extract sections of the paper note relevant to the cluster to save token context and prevent limits."""
    lines = note_content.splitlines()
    relevant_lines = []
    
    # 1. Extract bibliographic identity (Section 1)
    in_bib = False
    for line in lines:
        if "Bibliographic" in line or "1. Bibliographic" in line:
            in_bib = True
        elif in_bib and (line.startswith("---") or line.startswith("### 2") or line.startswith("### G2") or line.startswith("### Country/Election") or line.startswith("### G1")):
            in_bib = False
        if in_bib:
            relevant_lines.append(line)
            
    # 2. Extract cluster specific section
    keywords = {
        "G1_PAID_ADS_OBJECT": ["Paid Ads", "G1", "Ads, Targeting"],
        "G2_TOPIC_MODELING_METHOD": ["Methodology", "G2", "Methodological Extraction"],
        "G3_PLATFORMIZATION_DIGITAL_POLITICS": ["Concept of Digitalization", "Platformization", "G3"],
        "G4_CHILE_LATAM_CASE_CONTEXT": ["Country/Election Context", "G4", "Chile/Region Context", "Chile Context"],
        "G5_ETHICS_MANIPULATION_RISK": ["Risks, Ethics", "G5", "Ethics & Manipulation"],
        "G6_DIGITAL_CAPITALISM_PLATFORM_POWER": ["Digital Capitalism", "G6"],
        "G7_VENUE_POSITIONING_PRECEDENT": ["Venue", "G7", "Journal & Positioning"]
    }
    
    kw_list = keywords.get(cluster_code, [])
    in_section = False
    for line in lines:
        if line.startswith("###") and any(kw in line for kw in kw_list):
            in_section = True
        elif in_section and line.startswith("###") and not any(kw in line for kw in kw_list):
            in_section = False
        if in_section:
            relevant_lines.append(line)
            
    # 3. Extract specific bracket questions under Section 4
    in_question = False
    short_code = cluster_code.split('_')[0]  # e.g., G3
    for line in lines:
        if short_code in line and (line.startswith("**[") or line.startswith("*   **[")):
            in_question = True
        elif in_question and (line.startswith("**[") or line.startswith("*   **[") or line.startswith("###") or line.startswith("---")):
            in_question = False
        if in_question:
            relevant_lines.append(line)
            
    extracted = "\n".join(relevant_lines).strip()
    return extracted


def generate_cluster_note(client: TogetherAIClient, cluster_code: str, papers: List[Dict[str, Any]], output_dir: Path, model: str) -> bool:
    """Generate a single cluster synthesis note."""
    cluster_file_prefix, cluster_label = CLUSTER_KEYS[cluster_code]
    cluster_def = CLUSTER_DEFINITIONS[cluster_code]
    cluster_qs = CLUSTER_QUESTIONS[cluster_code]
    
    logger.info(f"Generating cluster note for: {cluster_label} ({cluster_code})")
    
    # Gather relevant paper notes
    relevant_papers = []
    for p in papers:
        # Check if cluster_code is listed in paper's YAML cluster list
        if cluster_code in p["clusters"]:
            relevant_papers.append(p)
            
    if not relevant_papers:
        logger.warning(f"No papers found for cluster {cluster_code}.")
        return False
        
    logger.info(f"Cluster {cluster_code} has {len(relevant_papers)} papers.")
    
    # Compile sources content
    papers_text = ""
    for idx, p in enumerate(relevant_papers):
        # Exclude YAML frontmatter to save tokens and focus on content
        content_parts = p["content"].split('---', 2)
        body = content_parts[2].strip() if len(content_parts) >= 3 else p["content"]
        
        # Extract only relevant sections
        relevant_body = extract_relevant_sections(body, cluster_code)
        if len(relevant_body) < 100:
            relevant_body = body
            
        papers_text += f"\n\n=========================================\n"
        papers_text += f"SOURCE NOTE: {p['filename']} ({p['author_year']})\n"
        papers_text += f"=========================================\n\n{relevant_body}\n"
        
    system_prompt = f"""You are an advanced research assistant compiling a literature synthesis.
You will compile a cluster synthesis note for the cluster: {cluster_label} ({cluster_code}).

Cluster Definition:
{cluster_def}

Format your output EXACTLY as this Markdown template:

# {cluster_label}

## Cluster Definition
{cluster_def}

## Synthesis of Sources
[Write a thorough, deeply detailed synthesis addressing these specific questions: {cluster_qs}. You MUST cite specific papers by author and year, e.g. "Alvarez-Fuentes et al. (2024) argued...", based ONLY on the provided notes.]

## Cross-References to Paper Notes
[Write a list of bullet points using Obsidian wikilinks [[NoteName]] (using the file base name without .md extension) and their specific relevance to the cluster. Do NOT surround the note links with backticks. Example:
- [[PDF_001_ALVAREZ-FUENTES_ETAL_2024]] - Specific relevance to the cluster.
]

## Gaps and Tensions
[Detail what the cluster literature fails to address or where sources contradict or disagree.]

Strict Execution Rules:
1. Preserve WikiLinks [[PDF_XXX_...]] for cross-references to the papers. Do NOT use backticks around WikiLinks.
2. Rely ONLY on the provided source notes. Do NOT speculate or introduce external knowledge.
3. Be specific, rigorous, and cite papers individually. Avoid generic statements like "the literature says".
4. Write a comprehensive, long, and detailed synthesis. Do not use placeholders.
"""

    prompt = f"{system_prompt}\n\nHere are the source paper notes to synthesize:\n{papers_text}"
    
    try:
        response = client.query_llm(prompt, model=model)
        output_path = output_dir / "cluster_notes" / f"{cluster_file_prefix}.md"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Ensure it has Obsidian frontmatter if needed, or just follow the template
        # The prompt instructions request the format starting with # [Cluster Label]
        output_path.write_text(response, encoding='utf-8')
        logger.info(f"Successfully saved cluster note to {output_path.name}")
        return True
    except Exception as e:
        logger.error(f"Failed to generate cluster note for {cluster_code}: {e}")
        return False


def generate_conceptual_framework_note(client: TogetherAIClient, cf_key: str, cluster_notes_dir: Path, output_dir: Path, model: str) -> bool:
    """Generate a single conceptual framework note using completed cluster notes as input."""
    cf_data = CONCEPTUAL_FRAMEWORKS[cf_key]
    cf_title = cf_data["title"]
    cf_goal = cf_data["goal"]
    cf_clusters = cf_data["clusters"]
    cf_cluster_files = cf_data["cluster_files"]
    
    logger.info(f"Generating conceptual framework note for: {cf_title}")
    
    # Read the relevant cluster notes
    cluster_notes_text = ""
    for c_file in cf_cluster_files:
        path = cluster_notes_dir / f"{c_file}.md"
        if path.exists():
            cluster_notes_text += f"\n\n=========================================\n"
            cluster_notes_text += f"CLUSTER NOTE: {c_file}.md\n"
            cluster_notes_text += f"=========================================\n\n{path.read_text(encoding='utf-8')}\n"
        else:
            logger.warning(f"Required cluster note {c_file}.md not found.")
            
    system_prompt = f"""You are a lead critical social theorist compiling a conceptual framework note for a publishable academic paper on digital politics and political campaigns.
The conceptual framework note you are writing is: {cf_title}.

Synthesis Goal:
{cf_goal}

Critical Theoretical Position (Fuchs/Digital Capitalism Lens):
- Adopt Christian Fuchs' perspective on digital capitalism as the critical lens.
- Do NOT remain neutral; position the literature in relation to:
  * Platform capitalism and data commodification.
  * Power asymmetries in digital political infrastructure.
  * The political economy of microtargeting.
  * Class, labor, and exploitation dimensions of platform-mediated campaigning.
- Emphasize and cite Christian Fuchs' specific chapters (PDF_057, PDF_058, PDF_059, PDF_060) where relevant to ground the critique.

You must format your output EXACTLY as this Markdown template:

# {cf_title}

## Theoretical Position (Fuchs/Digital Capitalism Lens)
[Write an explicit, non-neutral positioning statement based on Fuchs/digital capitalism lens.]

## Literature Integration
[Provide a deep, critical synthesis of the literature drawing from the provided cluster notes and citing specific papers by author and year.]

## Empirical Implications for Chile 2021
[Write a detailed, specific section on how this framework element guides the empirical analysis of Gabriel Boric's and other candidates' Facebook ads in Chile 2021.]

## Cross-References to Cluster Notes
[Provide Obsidian WikiLinks to the relevant cluster notes. Do NOT surround links with backticks. Example:
- [[NB0X_Cluster_Name]] - Specific relevance to this framework element.
]

## Cross-References to Paper Notes
[Provide Obsidian WikiLinks to the specific paper notes. Do NOT surround links with backticks. Example:
- [[PDF_XXX_...]] - Specific insight.
]

## Unresolved Questions
[What this framework element still needs to address or where theoretical tensions remain.]

Strict Execution Rules:
1. Preserve WikiLinks [[NoteName]] for cross-references to the cluster notes and paper notes. Do NOT use backticks around WikiLinks.
2. Rely on critical theoretical depth. Take a clear stance. Do NOT remain neutral.
3. Write a comprehensive, long, and detailed synthesis. Do not use placeholders or generic bullet outlines.
"""

    prompt = f"{system_prompt}\n\nHere are the cluster notes to integrate:\n{cluster_notes_text}"
    
    try:
        response = client.query_llm(prompt, model=model)
        output_path = output_dir / "conceptual_framework_notes" / f"{cf_title}.md"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        output_path.write_text(response, encoding='utf-8')
        logger.info(f"Successfully saved conceptual framework note to {output_path.name}")
        return True
    except Exception as e:
        logger.error(f"Failed to generate conceptual framework note for {cf_key}: {e}")
        return False


def verify_outputs(output_dir: Path) -> bool:
    """Verify that all files exist and contain required headers."""
    logger.info("Starting validation of generated notes...")
    success = True
    
    cluster_notes_dir = output_dir / "cluster_notes"
    conceptual_notes_dir = output_dir / "conceptual_framework_notes"
    
    required_cluster_headers = [
        "## Cluster Definition",
        "## Synthesis of Sources",
        "## Cross-References to Paper Notes",
        "## Gaps and Tensions"
    ]
    
    required_cf_headers = [
        "## Theoretical Position (Fuchs/Digital Capitalism Lens)",
        "## Literature Integration",
        "## Empirical Implications for Chile 2021",
        "## Cross-References to Cluster Notes",
        "## Cross-References to Paper Notes",
        "## Unresolved Questions"
    ]
    
    # 1. Verify Cluster Notes
    for code, (prefix, label) in CLUSTER_KEYS.items():
        path = cluster_notes_dir / f"{prefix}.md"
        if not path.exists():
            logger.error(f"Missing cluster note: {path.name}")
            success = False
            continue
            
        content = path.read_text(encoding='utf-8')
        if len(content.strip()) < 500:
            logger.error(f"Cluster note {path.name} is too short ({len(content)} chars).")
            success = False
            
        for h in required_cluster_headers:
            if h not in content:
                logger.error(f"Cluster note {path.name} is missing header: '{h}'")
                success = False
                
        # Check WikiLink formats
        if '`[[' in content or ']]`' in content:
            logger.warning(f"Cluster note {path.name} contains backticked WikiLinks.")
            
    # 2. Verify Conceptual Framework Notes
    for cf_key, data in CONCEPTUAL_FRAMEWORKS.items():
        path = conceptual_notes_dir / f"{data['title']}.md"
        if not path.exists():
            logger.error(f"Missing conceptual framework note: {path.name}")
            success = False
            continue
            
        content = path.read_text(encoding='utf-8')
        if len(content.strip()) < 500:
            logger.error(f"Conceptual framework note {path.name} is too short ({len(content)} chars).")
            success = False
            
        for h in required_cf_headers:
            if h not in content:
                logger.error(f"Conceptual framework note {path.name} is missing header: '{h}'")
                success = False
                
        # Check WikiLink formats
        if '`[[' in content or ']]`' in content:
            logger.warning(f"Conceptual framework note {path.name} contains backticked WikiLinks.")
            
    if success:
        logger.info("All output files successfully generated and verified!")
    else:
        logger.error("Validation failed for some notes. See logs above.")
    return success


def main():
    parser = argparse.ArgumentParser(description="Integrate Literature Notes")
    parser.add_argument("--excel_path", required=True, help="Path to RA_NotebookLM_Obsidian_Registry.xlsx")
    parser.add_argument("--papers_dir", required=True, help="Directory containing individual paper md files")
    parser.add_argument("--output_dir", required=True, help="Directory to save integration files")
    parser.add_argument("--model", default="moonshotai/Kimi-K2.6", help="Together.ai model to use")
    
    args = parser.parse_args()
    
    env_vars = load_environment()
    
    client = TogetherAIClient(
        base_url=env_vars["OPEN_API_BASE"],
        api_key=env_vars["OPEN_API_KEY"]
    )
    
    papers_dir = Path(args.papers_dir)
    output_dir = Path(args.output_dir)
    cluster_notes_dir = output_dir / "cluster_notes"
    
    # Load papers metadata
    papers = load_papers_metadata(papers_dir)
    if not papers:
        logger.error(f"No paper notes found in {papers_dir}.")
        return
        
    # Phase 1: Cluster Synthesis Notes
    logger.info("=========================================")
    logger.info("PHASE 1: GENERATING CLUSTER NOTES")
    logger.info("=========================================")
    for cluster_code in CLUSTER_KEYS.keys():
        generate_cluster_note(client, cluster_code, papers, output_dir, args.model)
        
    # Phase 2: Conceptual Framework Notes
    logger.info("=========================================")
    logger.info("PHASE 2: GENERATING CONCEPTUAL FRAMEWORK NOTES")
    logger.info("=========================================")
    for cf_key in CONCEPTUAL_FRAMEWORKS.keys():
        generate_conceptual_framework_note(client, cf_key, cluster_notes_dir, output_dir, args.model)
        
    # Phase 3: Verification
    logger.info("=========================================")
    logger.info("PHASE 3: VERIFYING OUTPUTS")
    logger.info("=========================================")
    verify_outputs(output_dir)


if __name__ == "__main__":
    main()
