# ---------------------------------------------------------
# Big Data Simulation: API Polling & Retry Logic
# ---------------------------------------------------------

"""
Scenario: Our ETL job depends on a file arriving in an S3 bucket.
We will poll (check) the bucket 5 times. If it arrives, we proceed.
If not, we fail the job.
"""

max_checks = 5
current_check = 0
file_found = False

print("--- Starting S3 Bucket Polling ---")

while current_check < max_checks:
    current_check += 1
    print("Check " + str(current_check) + " of " + str(max_checks) + ": Looking for file...")

    if current_check == 3:
        file_found = True
        print("SUCCESS: Target file located in S3!")
        break

    print("WAITING: File not here yet. Sleeping...")

print("---")
if file_found:
    print("ACTION: Starting Spark data extraction...")
else:
    print("CRITICAL ERROR: File never arrived. Pipeline terminating.")