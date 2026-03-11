# Big Data Simulation: Transaction Routing Logic

"""
Scenario: We receive transaction data. We need to calculate the
final price after tax, and then check if this transaction
should be routed to the 'High Value' database table.
"""

# 1. Variables and Data
item_price = 450.00
quantity = 2
tax_rate = 0.08  # 8% tax
high_value_threshold = 1000.00

# 2. Arithmetic: Calculate the subtotal and total
subtotal = item_price * quantity
tax_amount = subtotal * tax_rate
final_total = subtotal + tax_amount

# 3. Assignment: Let's pretend there's a $15 shipping fee added at the end
final_total += 15.00

# 4. Comparison: Does this meet the threshold?
is_high_value = final_total >= high_value_threshold

# 5. Output Results
print("Processed Transaction:")
print("Final Total calculated: $", final_total)
print("Route to High Value Table?", is_high_value)