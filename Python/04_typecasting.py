# ---------------------------------------------------------
# Big Data Simulation: CSV Data Processing
# ---------------------------------------------------------

"""
Scenario: We read a line from a CSV file.
Everything is currently a string. We need to calculate the total cost.
"""

raw_item_name = "Wireless Mouse"
raw_price = "24.50"
raw_quantity = "3"

clean_price = float(raw_price)
clean_quantity = int(raw_quantity)

total_cost = clean_price * clean_quantity

log_message = "SUCCESS: Order for " + raw_item_name + " processed. Total: $" + str(total_cost)

print(log_message)