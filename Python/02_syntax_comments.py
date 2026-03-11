# ---------------------------------------------------------
# Big Data Simulation: Simple Data Filter
# ---------------------------------------------------------

"""
This script simulates checking a user's age
to see if they are eligible for a data survey.
"""

user_age = 25
user_name = "Alice"

if user_age > 18:
    print("Checking database for:", user_name)
    print("Status: User is an adult.")

    if user_age > 60:
        print("Category: Senior Citizen")
    else:
        print("Category: Adult")

print("--- End of Check ---")