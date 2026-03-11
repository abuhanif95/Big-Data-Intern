# ---------------------------------------------------------
# Big Data Simulation: Map-Filter-Reduce Pipeline
# ---------------------------------------------------------

from functools import reduce

"""
Scenario: We have a batch of raw log strings. Format: "STATUS:AMOUNT"
We need to calculate the total revenue of SUCCESSFUL transactions.
"""

raw_logs = ["SUCCESS:150", "FAILED:50", "SUCCESS:200", "SUCCESS:50", "ERROR:99"]

print("--- Starting Pipeline ---")

successful_logs = list(filter(lambda log: log.startswith("SUCCESS"), raw_logs))

transaction_amounts = list(map(lambda log: int(log.split(":")[1]), successful_logs))

total_revenue = reduce(lambda a, b: a + b, transaction_amounts)

print("Filtered Logs:", successful_logs)
print("Mapped Amounts:", transaction_amounts)
print("FINAL REVENUE: $" + str(total_revenue))