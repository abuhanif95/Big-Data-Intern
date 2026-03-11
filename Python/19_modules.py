# ---------------------------------------------------------
# Big Data Simulation: Pipeline Latency Calculation
# ---------------------------------------------------------

from datetime import datetime
import math as m
import time

print("--- ETL Job Started ---")

start_time = datetime.now()
print("Job triggered at: " + str(start_time))

time.sleep(2.3)

end_time = datetime.now()
print("Job finished at: " + str(end_time))

time_difference = end_time - start_time
exact_seconds = time_difference.total_seconds()

billed_seconds = m.ceil(exact_seconds)

print("---")
print("Exact runtime: " + str(exact_seconds) + " seconds")
print("Billed runtime (Rounded): " + str(billed_seconds) + " seconds")