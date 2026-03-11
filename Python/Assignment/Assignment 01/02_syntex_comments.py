# ---------------------------------------------------------
# Big Data Simulation: Simple Data Filter
# ---------------------------------------------------------

"""
This script simulates checking a user's age
to see if they are eligible for a data survey.
"""

user_age = 25
user_name = "Alice"

# Logic to check eligibility
if user_age > 18:
    # Everything inside here runs ONLY if age > 18
    print("Checking database for:", user_name)
    print("Status: User is an adult.")

    if user_age > 60:
        # This is a nested block (8 spaces deep)
        print("Category: Senior Citizen")
    else:
        print("Category: Adult")

# This line is NOT indented, so it runs no matter what
print("--- End of Check ---")