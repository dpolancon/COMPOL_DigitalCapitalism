#!/usr/bin/env python3
"""Paste markdown from clipboard and save to notes/questions/"""
import sys, pyperclip, re
from pathlib import Path

def save_note():
    content = pyperclip.paste() if len(sys.argv) == 1 else sys.argv[1]
    # Extract note_id from YAML frontmatter
    match = re.search(r'note_id:\s*"([^"]+)"', content)
    if not match:
        print("❌ Could not find note_id in frontmatter")
        return
    note_id = match.group(1)
    output_path = Path(f"notes/questions/{note_id}.md")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ Saved: {output_path}")

if __name__ == "__main__":
    save_note()