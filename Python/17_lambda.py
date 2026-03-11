# ---------------------------------------------------------
# Big Data Simulation: Inline Data Transformation
# ---------------------------------------------------------

"""
Scenario: We have a batch of temperature sensor data in Celsius.
We need a lightweight function to convert these to Fahrenheit.
Formula: (C * 9/5) + 32
"""

celsius_readings = [0.0, 10.0, 25.5, 100.0]
fahrenheit_readings = []

print("--- Starting Sensor Data Conversion ---")

c_to_f = lambda c: (c * 1.8) + 32

for temp in celsius_readings:
    converted_temp = c_to_f(temp)
    fahrenheit_readings.append(converted_temp)
    print("Celsius: " + str(temp) + " -> Fahrenheit: " + str(converted_temp))

print("---")
print("Final Transformed Dataset: " + str(fahrenheit_readings))