# ---------------------------------------------------------
# Big Data Simulation: CSV Data Processing
# ---------------------------------------------------------

"""
Scenario: We read a line from a CSV file.
Everything is currently a string. We need to calculate the total cost.
"""

# 1. EXTRACT: Raw data from CSV
raw_item_name = "Wireless Mouse"
raw_price = "24.50"
raw_quantity = "3"

# 2. TRANSFORM: Cast types so we can do math
# Price needs decimals, Quantity is a whole number
clean_price = float(raw_price)
clean_quantity = int(raw_quantity)

# 3. APPLY LOGIC: Calculate total
total_cost = clean_price * clean_quantity

# 4. LOAD / OUTPUT: Create a log message
# We must cast the numeric result BACK to a string to print it nicely
log_message = "SUCCESS: Order for " + raw_item_name + " processed. Total: $" + str(total_cost)

print(log_message)