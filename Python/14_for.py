# ---------------------------------------------------------
# Big Data Simulation: Transaction Log Scrubbing
# ---------------------------------------------------------

"""
Scenario: We have a list of raw transaction statuses from an API.
We need to normalize the text to uppercase for our Data Warehouse,
and filter out internal test records.
"""

raw_transactions = ["success", "failed", "INTERNAL", "pending", "success"]
clean_data = []

print("--- Starting Batch Transformation ---")

for txn in raw_transactions:
    if txn == "INTERNAL":
        print("SKIP: Internal test record ignored.")
        continue

    normalized_txn = txn.upper()
    clean_data.append(normalized_txn)
    print("PROCESSED: " + normalized_txn)

print("---")
print("Transformation Complete.")
print("Final Dataset ready for DB: " + str(clean_data))