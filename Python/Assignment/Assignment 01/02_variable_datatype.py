# ---------------------------------------------------------
# Big Data Simulation: Pipeline Configuration Variables
# ---------------------------------------------------------

"""
This script simulates setting up variables for a nightly
data processing pipeline.
"""

# Defining Variables (Python infers the data types dynamically)
pipeline_name = "Nightly_Sales_ETL"  # String
batch_size = 50000  # Integer (Rows per batch)
failure_threshold = 0.05  # Float (5% error rate allowed)

# Let's inspect our setup
print("--- Pipeline Config ---")
print("Job Name:", pipeline_name, "| Type:", type(pipeline_name))
print("Batch Size:", batch_size, "| Type:", type(batch_size))
print("Error Threshold:", failure_threshold, "| Type:", type(failure_threshold))

print("\n--- Testing Data Type Logic ---")
# Math works on ints and floats
next_batch = batch_size + 10000
print("Next batch size will be:", next_batch)

# ❌ What happens if we try to do math with a String?
# Uncomment the line below to see a TypeError in action!
# print(pipeline_name + 10)
