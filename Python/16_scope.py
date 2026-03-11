# ---------------------------------------------------------
# Big Data Simulation: Global Configs & Local Logic
# ---------------------------------------------------------

"""
Scenario: We have a global configuration for our target database.
Our extraction function will use local variables to process data,
but will read the global config to know where to route it.
"""

TARGET_DATABASE = "snowflake_prod_db"
BATCH_SIZE = 1000

def process_batch(batch_id):
    records_processed = BATCH_SIZE
    print("Batch [" + str(batch_id) + "] cleaned locally.")
    print("Routing " + str(records_processed) + " records to: " + TARGET_DATABASE)
    return True

print("--- Starting ETL Run ---")

process_batch(1)
process_batch(2)

print("--- ETL Complete ---")