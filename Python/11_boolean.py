# ---------------------------------------------------------
# Big Data Simulation: Data Quality Evaluation
# ---------------------------------------------------------

"""
Scenario: Before loading a record into our Data Warehouse,
it must pass two checks: amount > 0 and currency must be USD.
"""

amount = 150.75
currency = "USD"

is_positive = amount > 0
is_usd = (currency == "USD")
is_real = True

is_valid_record = is_positive and is_usd and is_real

print("--- Data Quality Check Results ---")
print("Transaction Amount: $" + str(amount))
print("Currency: " + currency)
print("Is amount positive? " + str(is_positive))
print("Is currency USD? " + str(is_usd))
print("Is record real? " + str(is_real))
print("---")
print("Final Decision - Valid Record? " + str(is_valid_record))