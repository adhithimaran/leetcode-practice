class Assignment:
    def __init__(self, name, grade_weight, due_date, estimated_hours, difficulty):
        """
        Initialize an assignment with various factors
        
        Parameters:
        name (str): Assignment name
        grade_weight (float): Percentage of final grade (0-100)
        due_date (datetime): When the assignment is due
        estimated_hours (float): Estimated hours to complete
        difficulty (int): Subjective difficulty rating (1-5)
        """
        self.name = name
        self.grade_weight = grade_weight
        self.due_date = due_date
        self.estimated_hours = estimated_hours
        self.difficulty = difficulty

def get_day_score(current_day, due_day):
    """
    Calculate priority score based on current day and due day
    Higher scores for:
    - Assignments due early in the week (to avoid weekend rush)
    - Current days earlier in the week (more time to work)
    """
    # Convert to integers (Monday = 0, Sunday = 6)
    current_weekday = current_day.weekday()
    due_weekday = due_day.weekday()
    
    # Prefer working on assignments due early in week
    due_day_score = 1 - (due_weekday / 7)
    
    # Higher priority if current day is early in week
    current_day_score = 1 - (current_weekday / 7)
    
    # Combine scores
    return (due_day_score + current_day_score) / 2

def prioritize_assignments(assignments):
    """
    Calculate priority scores for assignments based on multiple factors
    
    Returns list of assignments sorted by priority (highest first)
    """
    from datetime import datetime
    
    # Weights for different factors (can be adjusted)
    WEIGHT_GRADE = 0.35     # Grade weight importance
    WEIGHT_TIME = 0.25      # Time until due date importance
    WEIGHT_EFFORT = 0.15    # Estimated hours importance
    WEIGHT_DIFFICULTY = 0.1 # Difficulty importance
    WEIGHT_DAY = 0.15      # Day of week importance
    
    now = datetime.now()
    scored_assignments = []
    
    for assignment in assignments:
        # Calculate days until due
        days_until_due = (assignment.due_date - now).days
        
        # Calculate individual scores (normalized to 0-1 scale)
        grade_score = assignment.grade_weight / 100
        time_score = max(0, min(1, 1 - (days_until_due / 14)))  # Normalized over 2 weeks
        effort_score = min(1, assignment.estimated_hours / 20)   # Normalized over 20 hours
        difficulty_score = assignment.difficulty / 5
        day_score = get_day_score(now, assignment.due_date)
        
        # Calculate weighted total score
        total_score = (
            grade_score * WEIGHT_GRADE +
            time_score * WEIGHT_TIME +
            effort_score * WEIGHT_EFFORT +
            difficulty_score * WEIGHT_DIFFICULTY +
            day_score * WEIGHT_DAY
        )
        
        scored_assignments.append((assignment, total_score))
    
    # Sort by score in descending order
    scored_assignments.sort(key=lambda x: x[1], reverse=True)
    
    return scored_assignments

# Example usage
from datetime import datetime, timedelta

# Create sample assignments
assignments = [
    Assignment(
        "Final Project", 
        grade_weight=30,
        due_date=datetime.now() + timedelta(days=10),
        estimated_hours=15,
        difficulty=4
    ),
    Assignment(
        "Weekly Quiz", 
        grade_weight=5,
        due_date=datetime.now() + timedelta(days=2),
        estimated_hours=1,
        difficulty=2
    ),
    Assignment(
        "Research Paper", 
        grade_weight=20,
        due_date=datetime.now() + timedelta(days=7),
        estimated_hours=10,
        difficulty=5
    )
]

# Get prioritized assignments
prioritized = prioritize_assignments(assignments)

# Print results with more detailed information
print("\nPrioritized Assignments:")
print("-----------------------")
for assignment, score in prioritized:
    days_until = (assignment.due_date - datetime.now()).days
    due_day = assignment.due_date.strftime("%A")
    print(f"{assignment.name}: {score:.2f}")
    print(f"  Due: {due_day} (in {days_until} days)")
    print(f"  Grade Weight: {assignment.grade_weight}%")
    print(f"  Estimated Hours: {assignment.estimated_hours}")
    print(f"  Difficulty: {assignment.difficulty}/5")
    print()