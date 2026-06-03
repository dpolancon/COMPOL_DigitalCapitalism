#!/usr/bin/env python3
"""
Batch-save multiple question notes from Qwen/Continue output.
Usage:
  1. Copy Qwen's output (multiple notes separated by ---)
  2. Run: python scripts/save_notes_batch.py --clipboard
  OR
  1. Save Qwen output to a text file
  2. Run: python scripts/save_notes_batch.py --input output.txt
"""

import re, sys, argparse, pyperclip
from pathlib import Path

def extract_note_id(frontmatter):
    """Extract note_id from YAML frontmatter"""
    match = re.search(r'note_id:\s*["\']?([^"\']+)["\']?', frontmatter)
    return match.group(1) if match else None

def split_notes(content):
    """Split content into individual note blocks by --- delimiter"""
    # Remove leading/trailing whitespace
    content = content.strip()
    # Split by standalone --- lines (with optional whitespace)
    blocks = re.split(r'\n---\s*\n', content)
    return [b.strip() for b in blocks if b.strip()]

def save_note(content, output_dir="notes/questions"):
    """Save a single note block to file"""
    # Extract frontmatter (first YAML block)
    frontmatter_match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not frontmatter_match:
        print(f"⚠️  Skipping block: no valid YAML frontmatter found")
        return False
    
    frontmatter = frontmatter_match.group(1)
    note_id = extract_note_id(frontmatter)
    
    if not note_id:
        print(f"⚠️  Skipping block: could not extract note_id")
        return False
    
    # Create output path
    output_path = Path(output_dir) / f"{note_id}.md"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Write file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Saved: {output_path}")
    return True

def main():
    parser = argparse.ArgumentParser(description="Batch-save Qwen-generated question notes")
    parser.add_argument('--clipboard', action='store_true', help='Read from system clipboard')
    parser.add_argument('--input', type=str, help='Read from input file')
    parser.add_argument('--dry-run', action='store_true', help='Preview what would be saved without writing')
    args = parser.parse_args()
    
    # Get content
    if args.clipboard:
        content = pyperclip.paste()
        print("📋 Reading from clipboard...")
    elif args.input:
        with open(args.input, 'r', encoding='utf-8') as f:
            content = f.read()
        print(f"📄 Reading from {args.input}...")
    else:
        print("❌ Error: Specify --clipboard or --input <file>")
        sys.exit(1)
    
    # Split into notes
    notes = split_notes(content)
    print(f"🔍 Found {len(notes)} note block(s)")
    
    # Process each note
    saved = 0
    for i, note in enumerate(notes, 1):
        if args.dry_run:
            note_id = extract_note_id(note)
            print(f"  [{i}] Would save: {note_id or 'UNKNOWN'}.md")
        else:
            if save_note(note):
                saved += 1
    
    if not args.dry_run:
        print(f"\n🎉 Done: {saved}/{len(notes)} notes saved to notes/questions/")

if __name__ == "__main__":
    main()