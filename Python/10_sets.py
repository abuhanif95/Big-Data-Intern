# ---------------------------------------------------------
# Big Data Simulation: Delta Load Processing
# ---------------------------------------------------------

"""
Scenario: We are comparing yesterday's master product list against today's
incoming data feed to route records to the correct database table.
"""

master_db_ids = {"prod_100", "prod_101", "prod_102"}

daily_batch_raw = ["prod_101", "prod_103", "prod_104", "prod_101"]

daily_batch_clean = set(daily_batch_raw)

records_to_insert = daily_batch_clean - master_db_ids
records_to_update = daily_batch_clean & master_db_ids

print("--- ETL Routing Report ---")
print("New Records to INSERT:", records_to_insert)
print("Existing Records to UPDATE:", records_to_update)