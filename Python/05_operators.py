# ---------------------------------------------------------
# Big Data Simulation: Transaction Routing Logic
# ---------------------------------------------------------

"""
Scenario: We receive transaction data. We need to calculate the
final price after tax, and then check if this transaction
should be routed to the 'High Value' database table.
"""

item_price = 450.00
quantity = 2
tax_rate = 0.08
high_value_threshold = 1000.00

subtotal = item_price * quantity
tax_amount = subtotal * tax_rate
final_total = subtotal + tax_amount

final_total += 15.00

is_high_value = final_total >= high_value_threshold

print("Processed Transaction:")
print("Final Total calculated: $", final_total)
print("Route to High Value Table?", is_high_value)