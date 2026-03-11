# ---------------------------------------------------------
# Big Data Simulation: Cleaning a Server Log
# ---------------------------------------------------------

"""
Scenario: We receive a messy log line from a web server.
We need to extract the Date, Error Level, and User ID.
"""

raw_log = "   [2024/05/12] -- cRiTiCaL -- UserId:90210   \n"

clean_log = raw_log.strip().upper().replace("/", "-")
print("Cleaned String:", clean_log)

log_parts = clean_log.split(" -- ")

date_part = log_parts[0]
error_level = log_parts[1]
user_info = log_parts[2]

final_user_id = user_info[7:]

print("\nFinal Parsed Data:")
print("Date:", date_part)
print("Level:", error_level)
print("User ID:", final_user_id)