#!/usr/bin/env python3
"""
Standardize LeetCode filenames to snake_case
Usage: python rename_files.py [--dry-run]
"""

import re
from pathlib import Path
import argparse

FOLDERS = [
    "arrays-hashing",
    "backtracking", 
    "binary-search",
    "linked-list",
    "matrix",
    "sliding-window",
    "stack",
    "trees",
    "two-pointers"
]

def to_snake_case(name):
    """Convert CamelCase or any format to snake_case"""
    # Insert underscore before capital letters (except first char)
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    # Insert underscore before capital letters that follow lowercase
    s2 = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1)
    # Handle numbers
    s3 = re.sub('([a-zA-Z])([0-9])', r'\1_\2', s2)
    s4 = re.sub('([0-9])([a-zA-Z])', r'\1_\2', s3)
    # Convert to lowercase and clean up
    return s4.lower().replace('-', '_').replace(' ', '_')

def standardize_filenames(dry_run=True):
    """Rename all files to snake_case"""
    changes = []
    
    for folder in FOLDERS:
        folder_path = Path(folder)
        if not folder_path.exists():
            continue
        
        print(f"\nScanning {folder}/...")
        
        for py_file in folder_path.glob("*.py"):
            if py_file.name.startswith('__'):
                continue
            
            # Get new name
            old_name = py_file.name
            name_without_ext = py_file.stem
            new_name_stem = to_snake_case(name_without_ext)
            new_name = f"{new_name_stem}.py"
            
            # Skip if already correct
            if old_name == new_name:
                print(f"  ✓ {old_name} (already standardized)")
                continue
            
            new_path = py_file.parent / new_name
            
            # Check for conflicts
            if new_path.exists():
                print(f"  ⚠ {old_name} → {new_name} (CONFLICT: target exists!)")
                continue
            
            changes.append((py_file, new_path, old_name, new_name))
            
            if dry_run:
                print(f"  → {old_name} → {new_name}")
            else:
                py_file.rename(new_path)
                print(f"  ✓ Renamed: {old_name} → {new_name}")
    
    # Summary
    print(f"\n{'='*60}")
    if dry_run:
        print(f"DRY RUN: Found {len(changes)} files to rename")
        print(f"Run without --dry-run to apply changes")
    else:
        print(f"✓ Renamed {len(changes)} files")
        if changes:
            print(f"\nNext steps:")
            print(f"  1. Delete leetcode_progress.json")
            print(f"  2. Run: python scan_and_add.py")
            print(f"  3. Commit changes: git add . && git commit -m 'Standardize filenames'")
    
    return changes

def main():
    parser = argparse.ArgumentParser(description="Standardize LeetCode filenames")
    parser.add_argument('--dry-run', action='store_true', 
                       help='Show what would be renamed without making changes')
    args = parser.parse_args()
    
    print("LeetCode Filename Standardizer")
    print("="*60)
    
    if args.dry_run:
        print("DRY RUN MODE - No files will be changed")
    else:
        print("WARNING: This will rename files!")
        response = input("Continue? (yes/no): ")
        if response.lower() != 'yes':
            print("Aborted.")
            return
    
    standardize_filenames(dry_run=args.dry_run)

if __name__ == "__main__":
    main()