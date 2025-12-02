# 🚀 LeetCode Practice Repository

A systematic approach to tracking and reviewing LeetCode problems with automated workflows.

## 📊 Visual Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│                    🌅 START YOUR DAY                            │
│                   python workflow.py daily                       │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
        ┌─────────────────────────────────────────┐
        │  Shows:                                  │
        │  • 📊 Your stats (total/confident/redo)  │
        │  • 🔥 Problems due today                 │
        │  • 🔴 All redo problems                  │
        └─────────────────────────────────────────┘
                              │
                    ┌─────────┴─────────┐
                    │                   │
                    ▼                   ▼
        ┌──────────────────┐   ┌──────────────────┐
        │  NEW PROBLEM?    │   │  REVIEW PROBLEM? │
        └──────────────────┘   └──────────────────┘
                    │                   │
                    ▼                   ▼
    ┌───────────────────────┐   ┌──────────────────────┐
    │ python workflow.py    │   │ Solve the problem... │
    │ add <#> "<n>"        │   │                      │
    │ <topic> <difficulty>  │   └──────────────────────┘
    └───────────────────────┘           │
            │                           ▼
            │               ┌────────────────────────┐
            │               │ python workflow.py     │
            │               │ review <#> <status>    │
            │               │                        │
            │               │ Status:                │
            │               │ • confident (🟢)       │
            │               │ • review (🟡)          │
            │               │ • redo (🔴)            │
            │               └────────────────────────┘
            │                           │
            └───────────┬───────────────┘
                        ▼
        ┌─────────────────────────────────┐
        │   ✅ AUTO COMMITS TO GIT         │
        │   Updates leetcode_progress.json │
        └─────────────────────────────────┘
                        │
                        ▼
        ┌─────────────────────────────────┐
        │  📅 SPACED REPETITION SCHEDULE   │
        │                                  │
        │  🔴 redo      → review in 1 day  │
        │  🟡 review    → review in 7 days │
        │  🟢 confident → review in 30 days│
        └─────────────────────────────────┘
```

## 📁 Repository Structure

```
LEETCODE/
├── arrays-hashing/          # Array and hash table problems
├── backtracking/           # Backtracking problems
├── binary-search/          # Binary search problems
├── linked-list/            # Linked list problems
├── matrix/                 # Matrix problems
├── sliding-window/         # Sliding window problems
├── stack/                  # Stack problems
├── trees/                  # Tree problems
├── two-pointers/           # Two pointer problems
├── tracker.py              # Progress tracking system
├── workflow.py             # Workflow automation
├── scan_and_add.py         # Bulk import existing problems
├── rename_files.py         # Standardize filenames
└── leetcode_progress.json  # Your progress data (auto-generated)
```

## 🎯 Quick Start

### First Time Setup

1. **Standardize your filenames** (optional but recommended):
```bash
# See what would change
python rename_files.py --dry-run

# Apply changes
python rename_files.py
```

2. **Import existing problems**:
```bash
python scan_and_add.py
```

3. **Check your progress**:
```bash
python tracker.py list
python tracker.py stats
```

## 📝 Daily Workflow

### Morning Routine
```bash
# Check what needs review today
python workflow.py daily
```

### Adding a New Problem
```bash
# Format: python workflow.py add <number> "<name>" <topic> <difficulty>
python workflow.py add 16 "Three Sum Closest" two-pointers medium

# This will:
# 1. Create a new file in the correct folder
# 2. Add it to the tracker
# 3. Commit to git automatically
```

### After Solving/Reviewing
```bash
# Update status: redo, review, or confident
python workflow.py review 16 confident

# This will:
# 1. Update tracker with new status
# 2. Increment attempt count
# 3. Commit to git automatically
```

## 🛠️ Manual Commands

### Tracker Commands

```bash
# List all problems
python tracker.py list

# List only problems that need redo
python tracker.py list --status redo

# Show problems due for review
python tracker.py review

# Show statistics
python tracker.py stats

# Manually add a problem
python tracker.py add 42 "Trapping Rain Water" --status redo --difficulty hard --tags "two-pointers,stack"

# Update a problem
python tracker.py update 42 --status confident --notes "Finally got it!"
```

### Git Commands

```bash
# See uncommitted changes
git status

# Push your progress
git push

# View commit history
git log --oneline
```

## 📊 Status System

Your problems are tracked with three statuses:

- **redo** (🔴): Need to practice again soon
  - Review in: 1 day
  
- **review** (🟡): Understand but need occasional practice
  - Review in: 7 days
  
- **confident** (🟢): Mastered the problem
  - Review in: 30 days

## 📂 Topic Folders

When adding problems, use these topic keywords (they map to folders):

| Keywords | Folder |
|----------|--------|
| `array`, `arrays`, `hash`, `hashing` | arrays-hashing |
| `backtrack` | backtracking |
| `binary` | binary-search |
| `linked`, `list` | linked-list |
| `matrix` | matrix |
| `window`, `sliding` | sliding-window |
| `stack` | stack |
| `tree`, `trees` | trees |
| `pointer`, `pointers` | two-pointers |

### Adding New Topic Folders

Need a new topic category? Use the automated script:

```bash
# Format: python add_folder.py <folder-name> "<tags>" "<keywords>"
python add_folder.py dynamic-programming "dynamic-programming,dp" "dp,dynamic"
```

**Examples:**
```bash
# Add graphs folder
python add_folder.py graphs "graphs,graph,dfs,bfs" "graph,graphs,dfs,bfs"

# Add heap/priority queue folder
python add_folder.py heap "heap,priority-queue" "heap,pq,priority"

# Add greedy algorithms folder
python add_folder.py greedy "greedy" "greedy"
```

The script automatically:
- ✅ Creates the folder
- ✅ Updates `scan_and_add.py` and `workflow.py`
- ✅ Updates this README
- ✅ Makes it immediately usable in workflows

After running, commit the changes:
```bash
git add .
git commit -m "Add topic: <folder-name>"
git push
```

## 💡 Examples

### Example 1: New Problem Flow
```bash
# Start your day
python workflow.py daily

# Add a new problem you're working on
python workflow.py add 121 "Best Time to Buy and Sell Stock" array easy

# ... solve it in the created file ...

# Mark as confident after solving
python workflow.py review 121 confident
```

### Example 2: Review Flow
```bash
# Check what needs review
python workflow.py daily

# You see problem #15 needs review
# ... redo the problem ...

# If you struggled, keep as redo
python workflow.py review 15 redo

# If you got it easily, mark confident
python workflow.py review 15 confident
```

### Example 3: Just Checking Progress
```bash
# See everything
python tracker.py list

# See just the tough ones
python tracker.py list --status redo

# See your stats
python tracker.py stats
```

## 🔄 Spaced Repetition Schedule

The tracker automatically schedules reviews based on your confidence:

```
First attempt (redo)
    ↓ (1 day later)
Review again
    ↓ if confident
Confident status
    ↓ (30 days later)
Review again to maintain
```

## 🐛 Troubleshooting

**Problem: Git merge conflicts in leetcode_progress.json**
```bash
# Keep your version
git checkout --ours leetcode_progress.json
git add leetcode_progress.json
```

**Problem: Accidentally deleted leetcode_progress.json**
```bash
# Restore from git
git checkout HEAD -- leetcode_progress.json
```

**Problem: Want to start fresh**
```bash
# Delete progress file and re-scan
rm leetcode_progress.json
python scan_and_add.py
```

## 📈 Tracking Your Progress

Your `leetcode_progress.json` file tracks:
- Problem number and name
- Current status (redo/review/confident)
- Number of attempts
- Last review date
- Next scheduled review
- Difficulty and tags
- Personal notes

**This file is committed to git**, so your progress history is preserved!

## 🎓 Tips for Success

1. **Be honest with status updates** - If you struggled, mark as `redo`
2. **Do your daily checks** - Run `python workflow.py daily` each morning
3. **Add notes** - Use `--notes` to remember what was tricky
4. **Review old problems** - Don't just chase new problems
5. **Commit regularly** - The automation handles this, but double-check with `git status`

## 📞 Quick Reference

| What you want | Command |
|---------------|---------|
| Daily check | `python workflow.py daily` |
| Add new problem | `python workflow.py add <#> "<name>" <topic> <diff>` |
| Update after review | `python workflow.py review <#> <status>` |
| See all problems | `python tracker.py list` |
| See stats | `python tracker.py stats` |
| See what's due | `python tracker.py review` |

---

**Happy coding! 🎉**

Remember: Consistency > Intensity. Do a little every day!