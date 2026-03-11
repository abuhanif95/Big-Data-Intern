# ---------------------------------------------------------
# Big Data Simulation: Processing Key-Value Pairs
# ---------------------------------------------------------

"""
Scenario: We have received an aggregated data record from a Spark cluster.
The data is a tuple representing (Department, Total_Sales, Employee_Count).
We need to unpack this data and calculate the average sales per employee.
"""

department_metrics = ("Engineering", 1500000.00, 25)

dept_name, total_sales, emp_count = department_metrics

avg_sales = total_sales / emp_count

summary_log = "Department: " + dept_name + " | " + "Avg Sales per Employee: $" + str(avg_sales)

print(summary_log)