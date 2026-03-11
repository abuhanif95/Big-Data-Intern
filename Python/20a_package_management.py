# ---------------------------------------------------------
# Big Data Simulation: Third-Party API Extraction (Part A)
# ---------------------------------------------------------

"""
Scenario: We need to extract data from a public REST API.
Using the third-party 'requests' package.
"""

import requests

print("--- Starting API Extraction ---")

try:
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")

    if response.status_code == 200:
        print("SUCCESS: Connected to API.")

        user_data = response.json()

        extracted_name = user_data.get("name")
        extracted_city = user_data["address"]["city"]

        print("Extracted User: " + extracted_name)
        print("Location: " + extracted_city)
    else:
        print("FAILED: API returned status code " + str(response.status_code))

except Exception as e:
    print("CRITICAL ERROR: Is the 'requests' library installed?")
    print(e)