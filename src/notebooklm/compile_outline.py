import os
import re
from pathlib import Path

def extract_cf_sections(content: str) -> str:
    """Extract sections from Conceptual Framework notes:
    - Theoretical Position (Fuchs/Digital Capitalism Lens)
    - Empirical Implications for Chile 2021
    """
    sections = {}
    current_header = None
    current_content = []
    
    lines = content.splitlines()
    for line in lines:
        if line.startswith('## '):
            if current_header:
                sections[current_header] = "\n".join(current_content).strip()
            current_header = line.replace('## ', '').strip()
            current_content = []
        elif current_header:
            current_content.append(line)
            
    if current_header:
        sections[current_header] = "\n".join(current_content).strip()
        
    extracted = []
    # Match various forms of Theoretical Position header
    theory_hdr = [h for h in sections.keys() if 'Theoretical Position' in h]
    if theory_hdr:
        extracted.append(f"  - *Theoretical Position*: {sections[theory_hdr[0]]}")
    else:
        extracted.append("  - *Theoretical Position*: (Not found)")
        
    # Match various forms of Empirical Implications header
    emp_hdr = [h for h in sections.keys() if 'Empirical Implications' in h]
    if emp_hdr:
        extracted.append(f"  - *Empirical Implications*: {sections[emp_hdr[0]]}")
    else:
        extracted.append("  - *Empirical Implications*: (Not found)")
        
    return "\n".join(extracted)

def extract_nb_sections(content: str) -> str:
    """Extract sections from Cluster notes:
    - Synthesis of Sources
    - Gaps and Tensions
    """
    sections = {}
    current_header = None
    current_content = []
    
    lines = content.splitlines()
    for line in lines:
        if line.startswith('## '):
            if current_header:
                sections[current_header] = "\n".join(current_content).strip()
            current_header = line.replace('## ', '').strip()
            current_content = []
        elif current_header:
            current_content.append(line)
            
    if current_header:
        sections[current_header] = "\n".join(current_content).strip()
        
    extracted = []
    synth_hdr = [h for h in sections.keys() if 'Synthesis of Sources' in h]
    if synth_hdr:
        extracted.append(f"  - *Synthesis of Sources*: {sections[synth_hdr[0]]}")
    else:
        extracted.append("  - *Synthesis of Sources*: (Not found)")
        
    gaps_hdr = [h for h in sections.keys() if 'Gaps' in h]
    if gaps_hdr:
        extracted.append(f"  - *Gaps and Tensions*: {sections[gaps_hdr[0]]}")
    else:
        extracted.append("  - *Gaps and Tensions*: (Not found)")
        
    return "\n".join(extracted)

def extract_pdf_sections(content: str) -> str:
    """Extract sections from Paper notes:
    - Bibliographic Identity (Title, Authors, Journal)
    - Method / Method & Corpus
    - Core Claims
    """
    # Split content into sections by h3 headers (### )
    sections = {}
    current_header = None
    current_content = []
    
    lines = content.splitlines()
    for line in lines:
        if line.startswith('### '):
            if current_header:
                sections[current_header] = "\n".join(current_content).strip()
            current_header = re.sub(r'^###\s*(?:\*\*)?\s*(?:\d+\.)?\s*', '', line).strip()
            current_header = current_header.strip('*').strip().lower()
            current_content = []
        elif current_header:
            current_content.append(line)
            
    if current_header:
        sections[current_header] = "\n".join(current_content).strip()

    if not sections:
        return "  - *Key Details*: Could not parse section headers."

    bibliographic_text = ""
    identity_keys = [k for k in sections.keys() if 'identity' in k or 'bibliographic' in k or 'citation' in k]
    if identity_keys:
        sec_text = sections[identity_keys[0]]
        # Try parsing single-line citation first (with/without colon)
        for line in sec_text.splitlines():
            m = re.search(r'\*\*(?:Bibliographic\s+|Source\s+)?Identity:?\*\*\s*(.*?)$', line, re.IGNORECASE)
            if m:
                identity_line = m.group(1).strip()
                identity_line = re.sub(r'^[\s*\t\-]+', '', identity_line).strip()
                # Check if it has a valid value
                if len(identity_line) > 5:
                    bibliographic_text = identity_line
                    break
                
        if not bibliographic_text:
            # Check for nested fields
            title_match = re.search(r'\*\*(?:Chapter\s+|Book\s+)?Title:\*\*\s*(.*?)$', sec_text, re.MULTILINE | re.IGNORECASE)
            if not title_match:
                title_match = re.search(r'\*\*Title:\*\*\s*(.*?)$', sec_text, re.MULTILINE | re.IGNORECASE)
                
            authors_match = re.search(r'\*\*(?:Author|Authors):\*\*\s*(.*?)$', sec_text, re.MULTILINE | re.IGNORECASE)
            
            venue_match = re.search(r'\*\*Journal:\*\*\s*(.*?)$', sec_text, re.MULTILINE | re.IGNORECASE)
            if not venue_match:
                venue_match = re.search(r'\*\*Book\s+Title:\*\*\s*(.*?)$', sec_text, re.MULTILINE | re.IGNORECASE)
            if not venue_match:
                venue_match = re.search(r'\*\*Book:\*\*\s*(.*?)$', sec_text, re.MULTILINE | re.IGNORECASE)
            if not venue_match:
                venue_match = re.search(r'\*\*Publisher:\*\*\s*(.*?)$', sec_text, re.MULTILINE | re.IGNORECASE)
            
            title = title_match.group(1).strip() if title_match else "(Unknown Title)"
            authors = authors_match.group(1).strip() if authors_match else "(Unknown Authors)"
            journal = venue_match.group(1).strip() if venue_match else "(Unknown Journal/Book)"
            
            # Clean formatting wrappers by removing all asterisks and underscores
            title = re.sub(r'[*_]', '', title).strip()
            journal = re.sub(r'[*_]', '', journal).strip()
            
            bibliographic_text = f"**{title}** by {authors} ({journal})"
            
    if not bibliographic_text:
        bibliographic_text = "(Unknown Bibliographic Identity)"

    # Capture method block
    method_block = ""
    method_keys = [k for k in sections.keys() if 'method' in k or 'details' in k]
    if not method_keys:
        method_keys = [k for k in sections.keys() if 'identity' in k or 'analysis' in k]
        
    if method_keys:
        sec_text = sections[method_keys[0]]
        m_match = re.search(r'\*\s+\*\*Method(?:ology| & Corpus)?:\*\*(.*?)(?=\*\s+\*\*|$)', sec_text, re.DOTALL | re.IGNORECASE)
        if m_match:
            method_block = m_match.group(1).strip()
            method_block = "\n".join(["    " + line.strip() for line in method_block.splitlines() if line.strip()])

    # Capture claims block
    claims_block = ""
    claims_keys = [k for k in sections.keys() if 'claims' in k]
    sole_claims_keys = [k for k in claims_keys if 'identity' not in k]
    if sole_claims_keys:
        claims_block = sections[sole_claims_keys[0]].strip()
    else:
        identity_keys = [k for k in sections.keys() if 'identity' in k or 'analysis' in k]
        if identity_keys:
            sec_text = sections[identity_keys[0]]
            c_match = re.search(r'\*\s+\*\*Core Claims:\*\*(.*?)(?=\*\s+\*\*|$)', sec_text, re.DOTALL | re.IGNORECASE)
            if c_match:
                claims_block = c_match.group(1).strip()

    if claims_block:
        claims_block = "\n".join(["    " + line.strip() for line in claims_block.splitlines() if line.strip()])

    extracted = []
    extracted.append(f"  - *Bibliographic Identity*: {bibliographic_text}")
    if method_block:
        extracted.append(f"  - *Methodology*:\n{method_block}")
    if claims_block:
        extracted.append(f"  - *Core Claims*:\n{claims_block}")
        
    return "\n".join(extracted)

def main():
    vault_dir = Path("compol_digital_capitalism_vault")
    outline_path = vault_dir / "30_Drafts" / "02_ConceptualFramework_Integrated_Detailed_Outline.md"
    
    if not outline_path.exists():
        print(f"Outline file not found at {outline_path}")
        return
        
    # Standard outline reset list:
    print(f"Reading outline file from {outline_path}")
    outline_content = outline_path.read_text(encoding='utf-8')
    
    lines = outline_content.splitlines()
    new_lines = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        match = re.match(r'^(\s*)-\s+\[\[(.*?)\]\]\s+\(from\s+`(.*?)`\):', line)
        if match:
            indent = match.group(1)
            note_name = match.group(2)
            relative_path = match.group(3)
            
            print(f"Resolving: [[{note_name}]] from path {relative_path}")
            
            # Reconstruct full path
            full_path = vault_dir / relative_path
            
            # Find and read the file
            if not full_path.exists():
                # Fallback search
                found = False
                for parent_dir in ["conceptual_framework_notes", "cluster_notes", "papers"]:
                    test_path = vault_dir / "10_Literature" / parent_dir / f"{note_name}.md"
                    if test_path.exists():
                        full_path = test_path
                        found = True
                        break
                if not found:
                    print(f"WARNING: File {note_name}.md not found anywhere in vault.")
                    new_lines.append(line)
                    i += 1
                    continue
            
            content = full_path.read_text(encoding='utf-8')
            
            # Extract content based on note type
            extracted_text = ""
            if "conceptual_framework_notes" in str(full_path):
                extracted_text = extract_cf_sections(content)
            elif "cluster_notes" in str(full_path):
                extracted_text = extract_nb_sections(content)
            elif "papers" in str(full_path):
                extracted_text = extract_pdf_sections(content)
            else:
                extracted_text = "  - *Content*: Transcluded general notes."
                
            # Add the header line
            new_lines.append(line)
            
            # Add the transcluded content (properly indented)
            indented_extracted = []
            for ext_line in extracted_text.splitlines():
                indented_extracted.append(f"{indent}  {ext_line}")
            new_lines.extend(indented_extracted)
            
            # Skip any existing transcluded bullet points that follow the matched line
            i += 1
            while i < len(lines):
                line_to_check = lines[i]
                if line_to_check.startswith(indent + "  ") or line_to_check.startswith(indent + "\t"):
                    i += 1
                elif not line_to_check.strip():
                    # It's an empty line. Let's see if there is more transcluded content after it.
                    has_more_transcluded = False
                    for j in range(i + 1, len(lines)):
                        next_line = lines[j]
                        if not next_line.strip():
                            continue
                        if next_line.startswith(indent + "  ") or next_line.startswith(indent + "\t"):
                            has_more_transcluded = True
                        break
                    if has_more_transcluded:
                        i += 1
                    else:
                        break
                else:
                    break
        else:
            new_lines.append(line)
            i += 1
            
    updated_content = "\n".join(new_lines)
    
    # Save the updated content
    outline_path.write_text(updated_content, encoding='utf-8')
    print(f"Successfully compiled outline with transcluded content to {outline_path}")

if __name__ == "__main__":
    main()
