# ---------------------------------------------------------
# Big Data Simulation: Object-Oriented Frameworks
# ---------------------------------------------------------

"""
Scenario: We are looking under the hood of a Big Data framework.
We will define a Blueprint (Class), create an Object from it,
and use its Methods to simulate reading data.
"""


class MockSparkSession:
    def __init__(self, app_name):
        self.app_name = app_name
        self.version = "3.5.0"
        self.is_connected = True

    def read_csv(self, file_path):
        if self.is_connected:
            print("Action: Reading data from " + file_path)
            return "Fake_DataFrame_Object"
        else:
            print("Error: Not connected to cluster.")
            return None  # Explicitly return None in the error case


spark = MockSparkSession(app_name="Daily_Sales_ETL")

print("--- Framework Initialized ---")

print("App Name: " + spark.app_name)
print("Spark Version: " + spark.version)

df = spark.read_csv("s3://bucket/sales_data.csv")

print("---")
print("Resulting output: " + str(df))