---
name: Pre-Flight Checklist & Execution
description: Conducting comprehensive pre-flight audits of automation pipelines against external data sources
source: auto-skill
extracted_at: '2026-06-02T20:12:26.123Z'
---

# Pre-Flight Checklist & Execution

This skill describes how to conduct comprehensive pre-flight audits of automation pipelines, cross-referencing registry data, manifest files, and code logic to ensure 100% readiness before production execution.

## Approach

### 1. Understand the Requirements
- Read the pre-flight prompt document to identify all audit objectives
- Identify required input files (registries, manifests, codebase, environment specs)
- Understand the output format and required deliverables

### 2. Registry vs Manifest Synchronization
- Cross-reference source IDs, filenames, and relative paths between Excel registry and CSV manifest
- Identify mismatches:
  - Files in manifest missing from registry
  - Files in registry missing from manifest
  - Path format inconsistencies (`\` vs `/` for Windows/Linux)
  - Subdirectory path prefixes (`CHANDLER_FUCHS_eds/` vs missing)
- Quantify mismatches to assess scope of fixes needed

### 3. Codebase Audit
- Review each Python module (api.py, extract_*.py, utils.py, notebooklm_cli.py)
- Check for critical issues:
  - Correct `logging.getLogger(__name__)` usage (not stray `name`)
  - Dynamic loading of configuration from external sources
  - Proper `argparse` argument setup
  - Path resolution using `pathlib.Path` for cross-platform compatibility
  - Sheet name targeting in Excel loading
  - Missing imports or syntax errors
- Assess import chains and dependency resolution

### 4. Environment & Dependency Verification
- Document exact terminal commands required to:
  1. Navigate to repository root in WSL/Linux environment
  2. Install/upgrade all Python dependencies
  3. Install browser automation tools (Playwright)
  4. Verify CLI authentication
- Format as copy-pasteable script blocks

### 5. Dry-Run Protocol Definition
- Define exact terminal command for single-file testing:
  - Target one specific `source_id` (e.g., `PDF_059`)
  - Specify all required paths: Excel, PDF directory, output directory
  - Include model parameter and logging level
- Create step-by-step verification checklist:
  - Output file created in correct location
  - YAML frontmatter contains required fields
  - Content extraction successful
  - Excel status updated correctly

### 6. Generate Actionable To-Do Checklist
- Create numbered tasks with specific actions
- Include commands for each task where applicable
- Order tasks logically: data fixes → environment setup → dry run → batch
- Add context gaps and warnings section

### 7. Execute Fixes Where Possible
- Create Python scripts to fix common issues programmatically
  - Path separator conversion in CSV files
  - File format fixes
  - Comment-based corrections
- Document all fixes made and remaining manual tasks

## Implementation Process

### Phase 1: Data Gathering
```bash
# Check file existence and structure
ls -la /path/to/excel/registry.xlsx
ls -la /path/to/pdf_manifest.csv
find /path/to/pdfs -type f | wc -l

# Examine code structure
ls -la src/notebooklm/*.py
head -20 src/notebooklm/*.py
```

### Phase 2: Cross-Reference Analysis
- Extract manifest data programmatically
- Query Excel registry structure
- Identify path mismatches quantitatively

### Phase 3: Code Review
- Read each module file
- Check function signatures and imports
- Verify proper logging patterns
- Identify any hardcoded paths or incorrect assumptions

### Phase 4: Output Generation
- Create report with all sections required by prompt
- Format as copy-pasteable Markdown
- Ensure all deliverables are present

### Phase 5: Execution (if applicable)
- Write and run fix scripts
- Document changes made
- Update playbook with remaining tasks

## Skill Triggers

Use this skill when:
- You receive a pre-flight check prompt requiring audit of automation pipelines
- You need to validate registry/manifest synchronization before batch processing
- You must identify blocking issues in codebases before production runs
- You're asked to generate executable to-do checklists and dry-run protocols
- Cross-referencing multiple data sources (Excel, CSV, code, manifests) is required

## Notes

- Always document confirmation numbers (how many paths fixed, files checked, etc.)
- Clearly distinguish between items resolved programmatically vs requiring manual intervention
- Keep terminal commands copy-paste-ready with full paths
- Add security warnings (Excel lockfiles, API key handling)