import sqlite3
import pandas as pd 

conn = sqlite3.connect('../baseball.db')
cursor = conn.cursor()
query = """
    SELECT playerID, teamID, yearID, HR
    FROM batting
    WHERE teamID = 'PHI' AND yearID = 1976 AND HR != 0
    ORDER BY HR desc;
"""
cursor.execute(query)
records = cursor.fetchall()
conn.close()
records_df = pd.DataFrame(records, columns = ["playerID", "teamID", "yearID", "HR"])

print(records_df)

