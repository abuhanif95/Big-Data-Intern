# ---------------------------------------------------------
# Big Data Simulation: MapReduce & Data Aggregation
# ---------------------------------------------------------

"""
Scenario: We are processing a batch of global e-commerce transactions.
The raw data arrives as a list of nested tuples: (Region, (Transaction_ID, Revenue)).
Some records dropped packets and have missing revenue (None).
We need to clean the data, aggregate total revenue by Region, and find the top performer.
"""

raw_transactions = [
    ("North America", ("TXN_101", 450.50)),
    ("Europe", ("TXN_102", 120.00)),
    ("North America", ("TXN_103", None)),
    ("Asia Pacific", ("TXN_104", 510.75)),
    ("Europe", ("TXN_105", 85.50)),
    ("North America", ("TXN_106", 150.00))
]

valid_records = [
    (region, revenue)
    for region, (txn_id, revenue) in raw_transactions
    if revenue is not None
]

regional_totals = {}
for region, revenue in valid_records:
    if region in regional_totals:
        regional_totals[region] += revenue
    else:
        regional_totals[region] = revenue

top_region = max(regional_totals, key=lambda k: regional_totals[k])

print("--- Global Sales Aggregation Report ---")
for region, total in regional_totals.items():
    print(f"Region: {region:<15} | Total Revenue: ${total:.2f}")

print("-" * 47)
print(f"🏆 Top Performing Region: {top_region} (${regional_totals[top_region]:.2f})")