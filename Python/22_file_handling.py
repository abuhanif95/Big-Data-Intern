# ---------------------------------------------------------
# Big Data Simulation: Writing and Reading a CSV
# ---------------------------------------------------------

"""
Scenario: Our transformation is complete. We have a list of clean IDs.
We need to WRITE them to a file, and then READ the file to verify.
"""

clean_user_ids = ["user_101", "user_102", "user_103"]
file_name = "target_users.csv"

print("--- Step 1: Writing Data (Load) ---")

with open(file_name, "w") as target_file:
    target_file.write("user_id\n")
    for uid in clean_user_ids:
        target_file.write(uid + "\n")
print("SUCCESS: File saved and automatically closed.")

print("\n--- Step 2: Reading Data (Verification) ---")

with open(file_name, "r") as source_file:
    saved_lines = source_file.readlines()
    for line in saved_lines:
        print("Found in file: " + line.strip())

print("Pipeline verified and complete.")