#!/usr/bin/env python3
"""
Add a new topic folder to the LeetCode repository
Usage: python add_folder.py <folder-name> <tag1,tag2> <keyword1,keyword2>

Example: python add_folder.py dynamic-programming "dynamic-programming,dp" "dp,dynamic"
"""

import sys
import re
from pathlib import Path

def update_file(filepath, pattern, replacement, multiline=False):
    """Update a file by replacing a pattern"""
    with open(filepath, 'r') as f:
        content = f.read()
    
    flags = re.MULTILINE if multiline else 0
    new_content = re.sub(pattern, replacement, content, flags=flags)
    
    with open(filepath, 'w') as f:
        f.write(new_content)
    
    return content != new_content

def add_folder(folder_name, tags, keywords):
    """Add a new topic folder and update all relevant files"""
    
    print(f"Adding new topic folder: {folder_name}")
    print("="*60)
    
    # Step 1: Create the folder
    folder_path = Path(folder_name)
    if folder_path.exists():
        print(f"✓ Folder '{folder_name}' already exists")
    else:
        folder_path.mkdir()
        print(f"✓ Created folder: {folder_name}/")
    
    # Step 2: Update scan_and_add.py
    print("\nUpdating scan_and_add.py...")
    scanner_file = Path("scan_and_add.py")
    
    if scanner_file.exists():
        # Find the FOLDER_TO_TAG dictionary and add new entry
        pattern = r'(FOLDER_TO_TAG = \{[^}]+)'
        replacement = f'\\1    "{folder_name}": "{tags}",\n'
        
        if update_file(scanner_file, pattern, replacement):
            print(f"  ✓ Added '{folder_name}' to FOLDER_TO_TAG")
        else:
            print(f"  ⚠ Could not update automatically - add manually:")
            print(f'     "{folder_name}": "{tags}",')
    else:
        print("  ⚠ scan_and_add.py not found")
    
    # Step 3: Update workflow.py
    print("\nUpdating workflow.py...")
    workflow_file = Path("workflow.py")
    
    if workflow_file.exists():
        # Add keywords to TOPIC_FOLDERS
        with open(workflow_file, 'r') as f:
            content = f.read()
        
        # Find end of TOPIC_FOLDERS dict
        pattern = r'(TOPIC_FOLDERS = \{[^}]+)(})'
        
        # Create entries for each keyword
        keyword_list = [kw.strip() for kw in keywords.split(',')]
        entries = '\n'.join([f'    "{kw}": "{folder_name}",' for kw in keyword_list])
        
        replacement = f'\\1    {entries}\n\\2'
        
        if update_file(workflow_file, pattern, replacement):
            print(f"  ✓ Added keywords to TOPIC_FOLDERS: {', '.join(keyword_list)}")
        else:
            print(f"  ⚠ Could not update automatically - add manually:")
            for kw in keyword_list:
                print(f'     "{kw}": "{folder_name}",')
    else:
        print("  ⚠ workflow.py not found")
    
    # Step 4: Update README.md
    print("\nUpdating README.md...")
    readme_file = Path("README.md")
    
    if readme_file.exists():
        # Find the topic table and add new row
        pattern = r'(\| `pointer`, `pointers` \| two-pointers \|)'
        keyword_display = ', '.join([f'`{kw}`' for kw in keyword_list])
        replacement = f'\\1\n| {keyword_display} | {folder_name} |'
        
        if update_file(readme_file, pattern, replacement):
            print(f"  ✓ Added to topic table in README")
        else:
            print(f"  ⚠ Could not update automatically - add manually to README topic table:")
            print(f'     | {keyword_display} | {folder_name} |')
    else:
        print("  ⚠ README.md not found")
    
    # Step 5: Update FOLDERS list in scan_and_add.py
    print("\nUpdating FOLDERS list in scan_and_add.py...")
    if scanner_file.exists():
        pattern = r'(FOLDERS = \[[^\]]+)'
        replacement = f'\\1    "{folder_name}",\n'
        
        if update_file(scanner_file, pattern, replacement):
            print(f"  ✓ Added to FOLDERS list")
        else:
            print(f"  ⚠ Add manually to FOLDERS list: \"{folder_name}\",")
    
    # Summary
    print("\n" + "="*60)
    print("✅ Setup complete!")
    print(f"\nYou can now use:")
    for kw in keyword_list:
        print(f'  python workflow.py add <#> "<n>" {kw} <difficulty>')
    print(f"\nFolder location: {folder_path}/")
    print("\nNext steps:")
    print("  1. Review the changes in scan_and_add.py, workflow.py, and README.md")
    print("  2. Run: python scan_and_add.py (if you have existing files to import)")
    print("  3. Commit: git add . && git commit -m 'Add topic: {folder_name}'")

def main():
    if len(sys.argv) != 4:
        print("Usage: python add_folder.py <folder-name> <tag1,tag2> <keyword1,keyword2>")
        print("\nExample:")
        print("  python add_folder.py dynamic-programming \"dynamic-programming,dp\" \"dp,dynamic\"")
        print("\nThis will:")
        print("  1. Create the folder")
        print("  2. Update scan_and_add.py with tags")
        print("  3. Update workflow.py with keywords")
        print("  4. Update README.md topic table")
        sys.exit(1)
    
    folder_name = sys.argv[1]
    tags = sys.argv[2]
    keywords = sys.argv[3]
    
    # Validate folder name (should be lowercase with hyphens)
    if not re.match(r'^[a-z0-9-]+$', folder_name):
        print("Error: Folder name should be lowercase with hyphens only")
        print("Example: dynamic-programming")
        sys.exit(1)
    
    add_folder(folder_name, tags, keywords)

if __name__ == "__main__":
    main()