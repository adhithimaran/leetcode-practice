#!/usr/bin/env python3
"""
LeetCode Workflow Automation
Usage:
    python workflow.py add 16 "Three Sum Closest" two-pointers medium
    python workflow.py review 16 confident
    python workflow.py daily
"""

import subprocess
import sys
import argparse
from pathlib import Path

TOPIC_FOLDERS = {
    "array": "arrays-hashing",
    "arrays": "arrays-hashing",
    "hash": "arrays-hashing",
    "hashing": "arrays-hashing",
    "backtrack": "backtracking",
    "binary": "binary-search",
    "linked": "linked-list",
    "list": "linked-list",
    "matrix": "matrix",
    "window": "sliding-window",
    "sliding": "sliding-window",
    "stack": "stack",
    "tree": "trees",
    "trees": "trees",
    "pointer": "two-pointers",
    "pointers": "two-pointers",
        "dp": "dynamic-programming",
    "dynamic": "dynamic-programming",
        "graph": "graphs",
    "graphs": "graphs",
    "dfs": "graphs",
    "bfs": "graphs",
        "heap": "heap",
    "pq": "heap",
    "priority": "heap",
        "greedy": "greedy",
}

def run_command(cmd, check=True):
    """Run a shell command"""
    print(f"→ {' '.join(cmd)}")
    result = subprocess.run(cmd, check=check, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    return result

def to_snake_case(name):
    """Convert name to snake_case for filename"""
    import re
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    s2 = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1)
    return s2.lower().replace(' ', '_').replace('-', '_')

def add_problem(number, name, topic, difficulty):
    """Add a new problem - creates file, adds to tracker, commits"""
    
    # Determine folder
    topic_lower = topic.lower()
    folder = TOPIC_FOLDERS.get(topic_lower, topic)
    folder_path = Path(folder)
    
    if not folder_path.exists():
        print(f"✗ Folder '{folder}' doesn't exist!")
        print(f"Available folders: {', '.join(set(TOPIC_FOLDERS.values()))}")
        return
    
    # Create filename
    filename = to_snake_case(name) + ".py"
    filepath = folder_path / filename
    
    # Check if file exists
    if filepath.exists():
        print(f"✗ File already exists: {filepath}")
        return
    
    # Create template file
    template = f'''"""
LeetCode #{number}: {name}
Difficulty: {difficulty.capitalize()}
Topic: {topic}

Problem:


Solution:

"""

class Solution(object):
    def solve(self):
        """
        :rtype: 
        """
        pass


# Test cases
if __name__ == "__main__":
    sol = Solution()
    # Add test cases here
'''
    
    filepath.write_text(template)
    print(f"✓ Created: {filepath}")
    
    # Add to tracker
    tags = folder.replace('-', ',')
    run_command([
        "python", "tracker.py", "add", 
        str(number), name,
        "--status", "redo",
        "--difficulty", difficulty,
        "--tags", tags
    ])
    
    # Git add and commit
    run_command(["git", "add", str(filepath), "leetcode_progress.json"])
    run_command(["git", "commit", "-m", f"Add: {number} - {name} ({difficulty})"])
    
    print(f"\n✓ Problem added successfully!")
    print(f"  File: {filepath}")
    print(f"  Next: Open the file and start coding!")

def review_problem(number, status):
    """Review a problem - updates tracker and commits"""
    
    # Update tracker
    run_command([
        "python", "tracker.py", "update",
        str(number),
        "--status", status,
        "--attempt"
    ])
    
    # Git commit
    run_command(["git", "add", "leetcode_progress.json"])
    run_command(["git", "commit", "-m", f"Review: {number} (now {status})"])
    
    print(f"\n✓ Review recorded and committed!")

def daily_check():
    """Show daily review list"""
    print("="*60)
    print("📅 DAILY LEETCODE CHECK")
    print("="*60)
    
    # Show stats
    run_command(["python", "tracker.py", "stats"])
    
    print()
    
    # Show what needs review
    run_command(["python", "tracker.py", "review"])
    
    print("\n" + "="*60)
    print("Commands:")
    print("  Review a problem: python workflow.py review <number> <status>")
    print("  Add new problem:  python workflow.py add <number> <name> <topic> <difficulty>")

def main():
    parser = argparse.ArgumentParser(description="LeetCode Workflow Automation")
    subparsers = parser.add_subparsers(dest="command", help="Commands")
    
    # Add problem
    add_parser = subparsers.add_parser("add", help="Add a new problem")
    add_parser.add_argument("number", type=int, help="Problem number")
    add_parser.add_argument("name", help="Problem name (in quotes)")
    add_parser.add_argument("topic", help="Topic/folder (e.g., two-pointers, array)")
    add_parser.add_argument("difficulty", choices=["easy", "medium", "hard"], 
                           help="Difficulty level")
    
    # Review problem
    review_parser = subparsers.add_parser("review", help="Review/update a problem")
    review_parser.add_argument("number", type=int, help="Problem number")
    review_parser.add_argument("status", choices=["redo", "review", "confident"],
                              help="New status")
    
    # Daily check
    subparsers.add_parser("daily", help="Show daily review list")
    
    args = parser.parse_args()
    
    if args.command == "add":
        add_problem(args.number, args.name, args.topic, args.difficulty)
    elif args.command == "review":
        review_problem(args.number, args.status)
    elif args.command == "daily":
        daily_check()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()