#!/usr/bin/env python3
"""
Scan existing LeetCode folders and add all problems to tracker
Usage: python scan_and_add.py
"""

import json
from pathlib import Path
from datetime import datetime, timedelta

PROGRESS_FILE = "leetcode_progress.json"
LEETCODE_DIR = "."  # Current directory

# Map folder names to tags
FOLDER_TO_TAG = {
    "arrays-hashing": "arrays,hashing",
    "backtracking": "backtracking",
    "binary-search": "binary-search",
    "linked-list": "linked-list",
    "matrix": "matrix",
    "sliding-window": "sliding-window",
    "stack": "stack",
    "trees": "trees",
    "two-pointers": "two-pointers"
}

def load_progress():
    """Load existing progress"""
    if Path(PROGRESS_FILE).exists():
        with open(PROGRESS_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_progress(data):
    """Save progress to JSON file"""
    with open(PROGRESS_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def calculate_next_review(status):
    """Calculate next review date"""
    today = datetime.now()
    if status == "redo":
        next_date = today + timedelta(days=1)
    elif status == "review":
        next_date = today + timedelta(days=7)
    else:  # confident
        next_date = today + timedelta(days=30)
    return next_date.strftime("%Y-%m-%d")

def clean_filename(filename):
    """Convert filename to readable problem name"""
    # Remove .py extension
    name = filename.replace('.py', '')
    # Replace underscores/hyphens with spaces
    name = name.replace('_', ' ').replace('-', ' ')
    # Capitalize words
    name = ' '.join(word.capitalize() for word in name.split())
    return name

def scan_and_add():
    """Scan folders and add all problems"""
    progress = load_progress()
    added_count = 0
    skipped_count = 0
    
    # Scan each folder
    for folder_name, tags in FOLDER_TO_TAG.items():
        folder_path = Path(LEETCODE_DIR) / folder_name
        
        if not folder_path.exists():
            continue
        
        print(f"\nScanning {folder_name}/...")
        
        # Find all .py files
        for py_file in folder_path.glob("*.py"):
            if py_file.name.startswith('__'):  # Skip __init__.py etc
                continue
            
            # Create problem ID from filename
            problem_id = py_file.stem  # filename without extension
            
            # Skip if already tracked
            if problem_id in progress:
                print(f"  ⊘ Skipped (already tracked): {problem_id}")
                skipped_count += 1
                continue
            
            # Add to progress
            problem_name = clean_filename(py_file.name)
            
            progress[problem_id] = {
                "number": None,  # Can be added later
                "name": problem_name,
                "status": "redo",  # Default to redo
                "difficulty": "medium",  # Default, can update later
                "tags": tags.split(','),
                "attempts": 0,
                "last_reviewed": None,
                "next_review": calculate_next_review("redo"),
                "notes": f"Auto-imported from {folder_name}/",
                "file_path": str(py_file.relative_to(LEETCODE_DIR))
            }
            
            print(f"  ✓ Added: {problem_name}")
            added_count += 1
    
    # Save all changes
    save_progress(progress)
    
    print(f"\n{'='*50}")
    print(f"✓ Scan complete!")
    print(f"  Added: {added_count} problems")
    print(f"  Skipped: {skipped_count} problems (already tracked)")
    print(f"  Total tracked: {len(progress)} problems")
    print(f"\nRun 'python tracker.py list' to see all problems")
    print(f"Run 'python tracker.py review' to see what needs review")

if __name__ == "__main__":
    print("Starting scan of LeetCode folders...")
    scan_and_add()