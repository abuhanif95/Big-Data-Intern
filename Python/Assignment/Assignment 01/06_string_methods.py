# Big Data Simulation: Cleaning a Server Log

"""
Scenario: We receive a messy log line from a web server.
We need to extract the Date, Error Level, and User ID.
"""

# 1. EXTRACT: The raw, messy string
raw_log = "   [2024/05/12] -- cRiTiCaL -- UserId:90210   \n"

# 2. TRANSFORM: Clean the text
# - Remove outer spaces/newlines
# - Convert to uppercase for standardization
# - Replace the weird slashes in the date with dashes
clean_log = raw_log.strip().upper().replace("/", "-")
print("Cleaned String:", clean_log)
# Currently looks like: [2024-05-12] -- CRITICAL -- USERID:90210

# 3. TRANSFORM: Split into components
# We see the data is separated by " -- "
log_parts = clean_log.split(" -- ")

# 4. LOAD (Ready for database)
date_part = log_parts[0]  # "[2024-05-12]"
error_level = log_parts[1]  # "CRITICAL"
user_info = log_parts[2]  # "USERID:90210"

# Let's slice the User ID to remove the "USERID:" prefix (which is 7 characters)
final_user_id = user_info[7:]

print("\nFinal Parsed Data:")
print("Date:", date_part)
print("Level:", error_level)
print("User ID:", final_user_id)