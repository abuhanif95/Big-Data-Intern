# ---------------------------------------------------------
# Big Data Simulation: Pipeline Configuration Variables
# ---------------------------------------------------------

"""
This script simulates setting up variables for a nightly
data processing pipeline.
"""

pipeline_name = "Nightly_Sales_ETL"
batch_size = 50000
failure_threshold = 0.05

print("--- Pipeline Config ---")
print("Job Name:", pipeline_name, "| Type:", type(pipeline_name))
print("Batch Size:", batch_size, "| Type:", type(batch_size))
print("Error Threshold:", failure_threshold, "| Type:", type(failure_threshold))

print("\n--- Testing Data Type Logic ---")
next_batch = batch_size + 10000
print("Next batch size will be:", next_batch)