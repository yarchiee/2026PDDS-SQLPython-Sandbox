"""
PDDS Workshop: Python & SQLite3 On-Hand Workshop
Database: AirlineDB_2026.DB
"""

# Importing the required libraries
import os
import sqlite3

# ==============================================================================
# STEP 1: Locate Database File
# Using os.path prevents "unable to open database" errors caused by different VS Code working dirs.
# ==============================================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "AirlineDB_2026.db")
if not os.path.exists(DB_PATH):
    print(f"[Error] Database file not found at: {DB_PATH}")
    print("Please make sure AirlineDB_2026.db is in the same folder as this script.")
    exit(1)

# ==============================================================================
# STEP 2: Connect to SQLite Database
# ==============================================================================

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# ==============================================================================
# STEP 3: Task & Try
# ==============================================================================
"""
Task 1: Total Flight Count -- Baseline Question
TODO:   Write a SQL query to count the total number of flights in the Flight table.
        Return the count as a single value.
"""

# Type your SQL query below
sql_task_1 = """
SELECT COUNT(*) FROM Flight;
"""

# Execute SQL query and fetch the result
cursor.execute(sql_task_1)

# Replace this with the code to execute the query and fetch the result
result_task_1 = cursor.fetchone()[0]

print("Task 1: Total Flight Count")
print(f"Total number of flights: {result_task_1}")
# Expected Output: 19

"""
Task 2: Flight Summary by Origin City
TODO:   Modify the SQL query below to show:
        origin city, count of flights, and average fare (rounded to 2 decimal places)
        Group by origin and order by flight count descending.
"""

# Type your SQL query below
sql_task_2 = """
SELECT origin, COUNT(*)  AS flight_count, ROUND(AVG(fare), 2) AS avg_fare
FROM Flight
GROUP BY origin
ORDER BY flight_count DESC;
"""
# Execute SQL query and fetch the result
cursor.execute(sql_task_2)

# Replace this with the code to execute the query and fetch the result
result_task_2 = cursor.fetchall()

print("Task 2: Flight Summary by Origin City")
print(f"{'Origin':<15} | {'Flight':<10} | {'Avg Fare ($)':<12}")
# Print all the results
for origin, count, avg_fare in result_task_2:
    print(f"{origin:<15} | {count:<10} | {avg_fare:<12.2f}")
# Expected Output:
# Origin City | Flight Count | Average Fare
# Los Angeles | 8 | 475.59
# ...

"""
Task 3: Join Flight with Aircraft
TODO:   Find which aircraft model is used for each flight from Madison.
"""

# Type your SQL query below
sql_task_3 = """
SELECT f.flno, f.destination, a.mname, a.model, f.fare
FROM Flight AS f
JOIN Aircraft AS a ON f.aid = a.aid
WHERE f.origin = 'Madison'
ORDER BY f.fare ASC;
"""

# Execute SQL query and fetch the result
cursor.execute(sql_task_3)

# Replace this with the code to execute the query and fetch the result
result_task_3 = cursor.fetchall()

print("Task 3: Join Flight with Aircraft")
print(f"{'Flight Number':<6} | {'Destination':<15} | {'Aircraft Name':<10} | {'Aircraft Model':<10} | {'Fare':<8}")
# Print all the results
for flno, dest, mname, model, fare in result_task_3:
    print(f"{flno:<13} | {dest:<15} | {mname:<13} | {model:<14} | {fare:<8.2f}")

# Expected Output:
# Flight Number | Destination | Aircraft Name | Aircraft Model | Fare
# 4884 | Chicago | Piper | Archer III | 112.45
# ...

# ==============================================================================
# STEP 4: Close Database Connection
# ==============================================================================

conn.close()