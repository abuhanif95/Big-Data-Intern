# ---------------------------------------------------------
# Big Data Simulation: Third-Party API Extraction (Part B)
# ---------------------------------------------------------

"""
Scenario: Fetching multiple users from a public REST API.
Using the third-party 'requests' package.
"""

import requests

url = "https://jsonplaceholder.typicode.com/users"

print("Sending request...")

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print("✅ Success! Here is the data for the first 3 users:\n")

    for user in data[:3]:
        print(f"Name: {user['name']}")
        print(f"Email: {user['email']}")
        print("-" * 20)
else:
    print(f"❌ Request failed, status code: {response.status_code}")