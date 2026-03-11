# ---------------------------------------------------------
# Big Data Simulation: Fault-Tolerant Data Parsing
# ---------------------------------------------------------

"""
Scenario: We are iterating through a list of raw string prices.
We need to convert them to floats for database ingestion.
If a record is corrupted, we must log it, default to 0.0,
and ensure the pipeline finishes the entire batch.
"""

raw_prices = ["19.99", "24.50", "FREE", "9.99"]
clean_prices = []

print("--- Starting Batch Processing ---")

for price in raw_prices:
    try:
        clean_price = float(price)
        clean_prices.append(clean_price)
        print("SUCCESS: Parsed $" + str(clean_price))

    except ValueError:
        print("DATA ERROR: Could not parse '" + price + "'. Defaulting to $0.0")
        clean_prices.append(0.0)

    finally:
        print(" -> Record processed and closed.")

print("---")
print("Batch Complete. Target DB List:", clean_prices)