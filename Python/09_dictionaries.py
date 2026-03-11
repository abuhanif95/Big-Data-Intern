# ---------------------------------------------------------
# Big Data Simulation: Nested JSON API Parsing
# ---------------------------------------------------------

"""
Scenario: We received a hierarchical JSON payload representing a customer's order.
We need to safely extract their shipping city and apply a discount if one exists.
"""

api_response = {
    "order_id": "ORD-99823A",
    "customer": {
        "name": "Alice",
        "shipping_address": {
            "city": "Seattle",
            "zip": "98101"
        }
    },
    "financials": {
        "cart_total": 150.0
    }
}

city = api_response["customer"]["shipping_address"]["city"]

total = api_response["financials"].get("cart_total", 0.0)
discount = api_response["financials"].get("discount_amount", 0.0)

final_price = total - discount

print("Routing order to: " + city)
print("Final Price after discounts: $" + str(final_price))