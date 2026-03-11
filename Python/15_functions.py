# ---------------------------------------------------------
# Big Data Simulation: Modular Data Cleaning
# ---------------------------------------------------------

"""
Scenario: We constantly receive messy currency strings from an external API
(like "$1,250.99"). We need a reusable function to clean them.
"""

def clean_currency_string(raw_price):
    step_1 = raw_price.strip()
    step_2 = step_1.replace("$", "")
    step_3 = step_2.replace(",", "")
    final_float = float(step_3)
    return final_float

raw_input_1 = "  $1,450.75"
raw_input_2 = "$99.99  "

print("--- Starting Transformation ---")

clean_price_1 = clean_currency_string(raw_input_1)
clean_price_2 = clean_currency_string(raw_input_2)

total_revenue = clean_price_1 + clean_price_2

print("Clean Price 1: " + str(clean_price_1))
print("Clean Price 2: " + str(clean_price_2))
print("Total Revenue: $" + str(total_revenue))