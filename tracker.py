#!/usr/bin/env python3
"""
LeetCode Progress Tracker
Usage:
    python tracker.py add 42 "Trapping Rain Water" --status redo --difficulty hard --tags "two-pointers,stack"
    python tracker.py update 42 --status confident
    python tracker.py list --status redo
    python tracker.py review
"""

import json
import argparse
from datetime import datetime, timedelta
from pathlib import Path

PROGRESS_FILE = "leetcode_progress.json"

def load_progress():
    """Load progress from JSON file"""
    if Path(PROGRESS_FILE).exists():
        with open(PROGRESS_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_progress(data):
    """Save progress to JSON file"""
    with open(PROGRESS_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def add_problem(number, name, status="redo", difficulty="medium", tags=None, notes=""):
    """Add a new problem to track"""
    progress = load_progress()
    problem_id = f"{int(number):04d}_{name.lower().replace(' ', '_')}"
    
    progress[problem_id] = {
        "number": int(number),
        "name": name,
        "status": status,
        "difficulty": difficulty,
        "tags": tags.split(',') if tags else [],
        "attempts": 1,
        "last_reviewed": datetime.now().strftime("%Y-%m-%d"),
        "next_review": calculate_next_review(status),
        "notes": notes
    }
    
    save_progress(progress)
    print(f"✓ Added: {problem_id}")

def update_problem(number, status=None, notes=None, increment_attempts=False):
    """Update an existing problem"""
    progress = load_progress()
    
    # Find problem by number
    problem_id = None
    for pid, data in progress.items():
        if data["number"] == int(number):
            problem_id = pid
            break
    
    if not problem_id:
        print(f"✗ Problem {number} not found!")
        return
    
    if status:
        progress[problem_id]["status"] = status
        progress[problem_id]["next_review"] = calculate_next_review(status)
    
    if notes:
        progress[problem_id]["notes"] = notes
    
    if increment_attempts:
        progress[problem_id]["attempts"] += 1
    
    progress[problem_id]["last_reviewed"] = datetime.now().strftime("%Y-%m-%d")
    
    save_progress(progress)
    print(f"✓ Updated: {problem_id} -> {status if status else 'notes updated'}")

def calculate_next_review(status):
    """Calculate next review date based on status"""
    today = datetime.now()
    
    if status == "redo":
        next_date = today + timedelta(days=1)
    elif status == "review":
        next_date = today + timedelta(days=7)
    elif status == "confident":
        next_date = today + timedelta(days=30)
    else:
        next_date = today + timedelta(days=3)
    
    return next_date.strftime("%Y-%m-%d")

def list_problems(status=None, due=False):
    """List problems, optionally filtered by status or due for review"""
    progress = load_progress()
    
    if not progress:
        print("No problems tracked yet!")
        return
    
    # Filter
    filtered = progress.items()
    if status:
        filtered = [(k, v) for k, v in filtered if v["status"] == status]
    
    if due:
        today = datetime.now().strftime("%Y-%m-%d")
        filtered = [(k, v) for k, v in filtered if v["next_review"] <= today]
    
    # Sort by number (or name if number is None)
    filtered = sorted(filtered, key=lambda x: (x[1]["number"] is None, x[1]["number"] or 0, x[0]))
    
    if not filtered:
        print(f"No problems found with filters: status={status}, due={due}")
        return
    
    # Display
    print(f"\n{'#':<6} {'Name':<35} {'Status':<12} {'Diff':<8} {'Next Review':<12} {'Attempts'}")
    print("-" * 95)
    
    for problem_id, data in filtered:
        num_display = str(data['number']) if data['number'] is not None else "-"
        print(f"{num_display:<6} {data['name']:<35} {data['status']:<12} {data['difficulty']:<8} {data['next_review']:<12} {data['attempts']}")
        if data['notes']:
            print(f"       Note: {data['notes']}")

def show_review_list():
    """Show problems due for review"""
    print("=== Problems Due for Review ===")
    list_problems(due=True)
    
    print("\n=== All Redo Problems ===")
    list_problems(status="redo")

def stats():
    """Show statistics"""
    progress = load_progress()
    
    if not progress:
        print("No problems tracked yet!")
        return
    
    total = len(progress)
    confident = len([p for p in progress.values() if p["status"] == "confident"])
    review_needed = len([p for p in progress.values() if p["status"] == "review"])
    redo = len([p for p in progress.values() if p["status"] == "redo"])
    
    print("\n=== LeetCode Progress Stats ===")
    print(f"Total problems: {total}")
    print(f"Confident: {confident} ({confident/total*100:.1f}%)")
    print(f"Review: {review_needed} ({review_needed/total*100:.1f}%)")
    print(f"Redo: {redo} ({redo/total*100:.1f}%)")
    
    # By difficulty
    difficulties = {}
    for p in progress.values():
        diff = p["difficulty"]
        difficulties[diff] = difficulties.get(diff, 0) + 1
    
    print("\nBy difficulty:")
    for diff, count in difficulties.items():
        print(f"  {diff}: {count}")

def main():
    parser = argparse.ArgumentParser(description="LeetCode Progress Tracker")
    subparsers = parser.add_subparsers(dest="command", help="Commands")
    
    # Add problem
    add_parser = subparsers.add_parser("add", help="Add a new problem")
    add_parser.add_argument("number", type=int, help="Problem number")
    add_parser.add_argument("name", help="Problem name")
    add_parser.add_argument("--status", choices=["redo", "review", "confident"], default="redo")
    add_parser.add_argument("--difficulty", choices=["easy", "medium", "hard"], default="medium")
    add_parser.add_argument("--tags", help="Comma-separated tags")
    add_parser.add_argument("--notes", default="", help="Additional notes")
    
    # Update problem
    update_parser = subparsers.add_parser("update", help="Update a problem")
    update_parser.add_argument("number", type=int, help="Problem number")
    update_parser.add_argument("--status", choices=["redo", "review", "confident"])
    update_parser.add_argument("--notes", help="Update notes")
    update_parser.add_argument("--attempt", action="store_true", help="Increment attempt count")
    
    # List problems
    list_parser = subparsers.add_parser("list", help="List problems")
    list_parser.add_argument("--status", choices=["redo", "review", "confident"])
    list_parser.add_argument("--due", action="store_true", help="Show only problems due for review")
    
    # Review
    subparsers.add_parser("review", help="Show problems due for review")
    
    # Stats
    subparsers.add_parser("stats", help="Show statistics")
    
    args = parser.parse_args()
    
    if args.command == "add":
        add_problem(args.number, args.name, args.status, args.difficulty, args.tags, args.notes)
    elif args.command == "update":
        update_problem(args.number, args.status, args.notes, args.attempt)
    elif args.command == "list":
        list_problems(args.status, args.due)
    elif args.command == "review":
        show_review_list()
    elif args.command == "stats":
        stats()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()