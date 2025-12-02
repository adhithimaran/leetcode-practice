#!/usr/bin/env python3
"""
Hide or reveal problem solutions
Usage:
    python solution.py hide <problem_number>   # Hide solution for redo
    python solution.py show <problem_number>   # Reveal solution after solving
    python solution.py hide-all-redo           # Hide all problems marked as redo
"""

import json
import sys
import re
from pathlib import Path

PROGRESS_FILE = "leetcode_progress.json"
HIDDEN_SUFFIX = ".hidden"

def load_progress():
    """Load progress from JSON"""
    if Path(PROGRESS_FILE).exists():
        with open(PROGRESS_FILE, 'r') as f:
            return json.load(f)
    return {}

def find_problem_file(problem_number):
    """Find the file for a given problem number"""
    progress = load_progress()
    
    for problem_id, data in progress.items():
        if data.get("number") == int(problem_number):
            file_path = data.get("file_path")
            if file_path and Path(file_path).exists():
                return Path(file_path), problem_id, data
    
    return None, None, None

def hide_solution(filepath):
    """Hide solution by moving file and creating a template"""
    hidden_path = Path(str(filepath) + HIDDEN_SUFFIX)
    
    # Check if already hidden
    if hidden_path.exists():
        print(f"⚠ Solution already hidden: {filepath}")
        return False
    
    # Read original file
    with open(filepath, 'r') as f:
        original_content = f.read()
    
    # Move original to .hidden
    filepath.rename(hidden_path)
    print(f"✓ Hidden solution: {filepath} → {hidden_path.name}")
    
    # Extract problem info from original
    problem_match = re.search(r'LeetCode #(\d+): (.+)', original_content)
    difficulty_match = re.search(r'Difficulty: (\w+)', original_content)
    topic_match = re.search(r'Topic: (.+)', original_content)
    
    problem_num = problem_match.group(1) if problem_match else "?"
    problem_name = problem_match.group(2) if problem_match else "Problem"
    difficulty = difficulty_match.group(1) if difficulty_match else "?"
    topic = topic_match.group(1) if topic_match else "?"
    
    # Create fresh template
    template = f'''"""
LeetCode #{problem_num}: {problem_name}
Difficulty: {difficulty}
Topic: {topic}

Problem:
[Try to solve from memory without looking at the hidden solution]

Solution approach:


Time complexity:
Space complexity:

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
    
# 💡 Your previous solution is hidden in {hidden_path.name}
# Run: python solution.py show {problem_num}  to reveal it after you're done
'''
    
    with open(filepath, 'w') as f:
        f.write(template)
    
    print(f"✓ Created fresh template: {filepath}")
    return True

def show_solution(filepath):
    """Restore hidden solution"""
    hidden_path = Path(str(filepath) + HIDDEN_SUFFIX)
    
    if not hidden_path.exists():
        print(f"⚠ No hidden solution found: {hidden_path}")
        return False
    
    # Backup current attempt if it exists
    if filepath.exists():
        backup_path = Path(str(filepath).replace('.py', '_attempt.py'))
        filepath.rename(backup_path)
        print(f"✓ Saved your attempt: {backup_path.name}")
    
    # Restore original
    hidden_path.rename(filepath)
    print(f"✓ Revealed solution: {filepath}")
    return True

def hide_all_redo():
    """Hide all problems marked as redo"""
    progress = load_progress()
    count = 0
    
    for problem_id, data in progress.items():
        if data.get("status") == "redo":
            file_path = data.get("file_path")
            if file_path and Path(file_path).exists():
                if hide_solution(Path(file_path)):
                    count += 1
    
    print(f"\n✓ Hidden {count} solution(s) marked as redo")

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python solution.py hide <problem_number>")
        print("  python solution.py show <problem_number>")
        print("  python solution.py hide-all-redo")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "hide-all-redo":
        hide_all_redo()
        return
    
    if len(sys.argv) < 3:
        print("Error: Missing problem number")
        sys.exit(1)
    
    problem_number = sys.argv[2]
    
    # Find the problem file
    filepath, problem_id, data = find_problem_file(problem_number)
    
    if not filepath:
        print(f"✗ Problem #{problem_number} not found in tracker")
        print("Run 'python tracker.py list' to see all problems")
        sys.exit(1)
    
    if command == "hide":
        print(f"Hiding solution for: {data['name']} (#{problem_number})")
        hide_solution(filepath)
        print(f"\n💡 To reveal later: python solution.py show {problem_number}")
    elif command == "show":
        print(f"Revealing solution for: {data['name']} (#{problem_number})")
        show_solution(filepath)
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

if __name__ == "__main__":
    main()