import sqlite3

connection = sqlite3.connect('database.db')

cur = connection.cursor()

print("Feedback entries:")
feedback_entries = cur.execute("SELECT * FROM feedback").fetchall()
for entry in feedback_entries:
    print(entry)

print("\nAnalysis entries:")
analysis_entries = cur.execute("SELECT * FROM analysis").fetchall()
for entry in analysis_entries:
    print(entry)

connection.close()
