# COMPOL Digital Capitalism - Repository Setup Script
# This script creates missing directories and configuration files
# SAFE: Won't delete existing data

$ErrorActionPreference = "Stop"
$repoRoot = "C:\ReposGitHub\COMPOL_DigitalCapitalism"

Write-Host "=== COMPOL Digital Capitalism Repository Setup ===" -ForegroundColor Cyan
Write-Host "Repository Root: $repoRoot" -ForegroundColor Gray
Write-Host ""

# Create src directory structure
Write-Host "[1/6] Creating src/ directory structure..." -ForegroundColor Yellow
$srcDirs = @(
    "src/notebooklm",
    "src/analysis",
    "src/utils",
    "output/figures",
    "output/tables",
    "output/drafts"
)

foreach ($dir in $srcDirs) {
    $fullPath = Join-Path $repoRoot $dir
    if (!(Test-Path $fullPath)) {
        New-Item -ItemType Directory -Path $fullPath -Force | Out-Null
        Write-Host "  Created: $dir" -ForegroundColor Green
    } else {
        Write-Host "  Already exists: $dir" -ForegroundColor Gray
    }
}

# Create .gitignore
Write-Host ""
Write-Host "[2/6] Creating .gitignore..." -ForegroundColor Yellow
$gitignorePath = Join-Path $repoRoot ".gitignore"
$gitignoreContent = @"
# Python
__pycache__/
*.py[cod]
`$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# Virtual environments
venv/
ENV/
env/
.venv

# Jupyter Notebook
.ipynb_checkpoints

# Obsidian
.obsidian/workspace
.obsidian/workspace.json
.obsidian/app.json
.obsidian/appearance.json
.obsidian/core-plugins.json
.obsidian/plugins/obsidian-git/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db
desktop.ini

# Data (keep raw data out of git)
data/raw/*
!data/raw/.gitkeep
data/processed/*
!data/processed/.gitkeep

# Large files
*.pdf
!literature/pdfs/.gitkeep
output/figures/*.png
output/figures/*.jpg
output/tables/*.csv

# API Keys and secrets
.env
*.key
secrets.json

# Logs
*.log
"@

Set-Content -Path $gitignorePath -Value $gitignoreContent -Encoding UTF8
Write-Host "  Created: .gitignore" -ForegroundColor Green

# Create .gitkeep files for empty directories
Write-Host ""
Write-Host "[3/6] Creating .gitkeep files..." -ForegroundColor Yellow
$gitkeepDirs = @(
    "data/raw",
    "data/processed",
    "literature/pdfs",
    "output/figures",
    "output/tables",
    "output/drafts",
    "src/notebooklm",
    "src/analysis",
    "src/utils"
)

foreach ($dir in $gitkeepDirs) {
    $fullPath = Join-Path $repoRoot $dir
    $gitkeepPath = Join-Path $fullPath ".gitkeep"
    if (!(Test-Path $gitkeepPath)) {
        New-Item -ItemType File -Path $gitkeepPath | Out-Null
        Write-Host "  Created: $dir/.gitkeep" -ForegroundColor Green
    }
}

# Create README.md
Write-Host ""
Write-Host "[4/6] Creating README.md..." -ForegroundColor Yellow
$readmePath = Join-Path $repoRoot "README.md"
$readmeContent = @"
# COMPOL: Digital Capitalism Research Project

## Overview
This repository contains the research project on Digital Capitalism, analyzing the 2021 Presidential Election Facebook Ads data through a heterodox macroeconomic lens.

## Repository Structure

\`\`\`
COMPOL_DigitalCapitalism/
├── vault/                      # Obsidian vault (knowledge management)
│   ├── 00_Inbox/               # Quick captures
│   ├── 10_Literature/          # Literature notes (auto-generated)
│   ├── 20_Project_Notes/       # Methodology & framework
│   └── 30_Drafts/              # Paper drafts
├── data/                       # Empirical data
│   ├── raw/                    # Original datasets
│   └── processed/              # Cleaned data
├── literature/                 # Academic references
│   ├── pdfs/                   # PDF files
│   └── pdf_manifest.csv        # Literature registry
├── src/                        # Source code
│   ├── notebooklm/             # NotebookLM automation scripts
│   ├── analysis/               # Empirical analysis code
│   └── utils/                  # Utility functions
├── output/                     # Generated outputs
│   ├── figures/                # Charts and visualizations
│   ├── tables/                 # Statistical tables
│   └── drafts/                 # Compiled paper drafts
└── legacy_repo/                # Original project (reference only)
\`\`\`

## Setup Instructions

### 1. Environment Setup
\`\`\`bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\\Scripts\\activate

# Install dependencies
pip install -r requirements.txt
\`\`\`

### 2. API Keys
Create a \`.env\` file in the root directory:
\`\`\`
TOGETHER_API_KEY=your_api_key_here
OPENAI_API_KEY=your_openai_key_if_needed
\`\`\`

### 3. Obsidian Vault
The vault is located at \`vault/\`. Open this folder in Obsidian.

## Workflow

### Literature Review Automation
\`\`\`bash
# Run NotebookLM extraction
python src/notebooklm/extract_literature.py --manifest literature/pdf_manifest.csv
\`\`\`

### Qwen Terminal Assistant
\`\`\`bash
# Query Qwen directly
python src/utils/qwen_cli.py "Your question here"
\`\`\`

### Analysis Pipeline
\`\`\`bash
# Run empirical analysis
python src/analysis/main_analysis.py
\`\`\`

## Git Protocol

- \`main\`: Stable, working version
- \`develop\`: Active development
- Feature branches: \`feature/description\`

## Dependencies
- Python 3.10+
- notebooklmpy
- pandas, numpy
- openai (for Together.ai API)
- obsidian (for knowledge management)

## License
Academic use - Please cite appropriately

## Contact
Your Name - your.email@institution.edu
"@

Set-Content -Path $readmePath -Value $readmeContent -Encoding UTF8
Write-Host "  Created: README.md" -ForegroundColor Green

# Create pyproject.toml
Write-Host ""
Write-Host "[5/6] Creating pyproject.toml..." -ForegroundColor Yellow
$pyprojectPath = Join-Path $repoRoot "pyproject.toml"
$pyprojectContent = @"
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "compol-digital-capitalism"
version = "0.1.0"
description = "Digital Capitalism Research - 2021 Presidential Election Facebook Ads Analysis"
readme = "README.md"
requires-python = ">=3.10"
license = {text = "MIT"}
authors = [
    {name = "Your Name", email = "your.email@institution.edu"}
]
keywords = ["digital capitalism", "political economy", "facebook ads", "elections"]
classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
]

dependencies = [
    "pandas>=2.0.0",
    "numpy>=1.24.0",
    "openai>=1.0.0",
    "python-dotenv>=1.0.0",
    "requests>=2.31.0",
    "pyyaml>=6.0",
    "tqdm>=4.65.0",
    "jupyter>=1.0.0",
    "notebook>=7.0.0",
    "matplotlib>=3.7.0",
    "seaborn>=0.12.0",
    "scipy>=1.10.0",
    "statsmodels>=0.14.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.3.0",
    "black>=23.0.0",
    "flake8>=6.0.0",
    "mypy>=1.0.0",
]
notebooklm = [
    "google-genai>=0.1.0",
    "PyPDF2>=3.0.0",
    "pdfplumber>=0.10.0",
]

[project.scripts]
qwen-cli = "src.utils.qwen_cli:main"

[tool.setuptools.packages.find]
where = ["."]
include = ["src*"]

[tool.black]
line-length = 100
target-version = ['py310', 'py311']

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = "test_*.py"

[tool.mypy]
python_version = "3.10"
warn_return_any = true
warn_unused_configs = true
"@

Set-Content -Path $pyprojectPath -Value $pyprojectContent -Encoding UTF8
Write-Host "  Created: pyproject.toml" -ForegroundColor Green

# Create requirements.txt
Write-Host ""
Write-Host "[6/6] Creating requirements.txt..." -ForegroundColor Yellow
$requirementsPath = Join-Path $repoRoot "requirements.txt"
$requirementsContent = @"
# Core Data Science
pandas>=2.0.0
numpy>=1.24.0
scipy>=1.10.0

# API & LLM Integration
openai>=1.0.0
python-dotenv>=1.0.0
requests>=2.31.0

# Data Processing
pyyaml>=6.0
tqdm>=4.65.0
PyPDF2>=3.0.0
pdfplumber>=0.10.0

# Visualization
matplotlib>=3.7.0
seaborn>=0.12.0

# Statistical Analysis
statsmodels>=0.14.0

# Development
jupyter>=1.0.0
notebook>=7.0.0
"@

Set-Content -Path $requirementsPath -Value $requirementsContent -Encoding UTF8
Write-Host "  Created: requirements.txt" -ForegroundColor Green

# Create .env.example
Write-Host ""
Write-Host "[Bonus] Creating .env.example..." -ForegroundColor Yellow
$envExamplePath = Join-Path $repoRoot ".env.example"
$envExampleContent = @"
# Together.ai API Key (for Qwen models)
TOGETHER_API_KEY=your_together_api_key_here

# Optional: OpenAI API Key (if needed for comparison)
OPENAI_API_KEY=your_openai_api_key_here

# Optional: Google API Key (for NotebookLM if using official API)
GOOGLE_API_KEY=your_google_api_key_here
"@

Set-Content -Path $envExamplePath -Value $envExampleContent -Encoding UTF8
Write-Host "  Created: .env.example" -ForegroundColor Green

Write-Host ""
Write-Host "=== Setup Complete! ===" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "1. Review the created files in: $repoRoot"
Write-Host "2. Initialize git: cd $repoRoot && git init"
Write-Host "3. Install dependencies: pip install -r requirements.txt"
Write-Host "4. Create .env file with your API keys (copy from .env.example)"
Write-Host "5. Port your notebooklm scripts from Financialization_LandRent/05_scripts"
Write-Host ""