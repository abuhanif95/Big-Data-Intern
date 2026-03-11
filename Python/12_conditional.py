# ---------------------------------------------------------
# Big Data Simulation: Pipeline Execution Gateway
# ---------------------------------------------------------

"""
Scenario: A Spark job is triggered. The script must check the
environment status and data size before allowing computation to start.
"""

system_status = "Online"
user_role = "Data_Engineer"
incoming_data_gb = 150

if system_status != "Online":
    print("BLOCKER: System is undergoing maintenance. Try again later.")
elif user_role != "Data_Engineer":
    print("BLOCKER: Unauthorized user. Access denied.")
else:
    print("Status Check: Passed. Checking data volume...")

    if incoming_data_gb > 500:
        print("ACTION: Data is massive. Triggering High-Memory Cluster.")
    elif incoming_data_gb > 100:
        print("ACTION: Data is moderate. Triggering Standard Cluster.")
    else:
        print("ACTION: Data is small. Processing on Local Node.")

    print("SUCCESS: Pipeline started.")