import sqlite3

connection = sqlite3.connect('database.db')

cur = connection.cursor()

print(cur.execute("SELECT * FROM feedback").fetchall())

print(cur.execute("SELECT * FROM analysis").fetchall())

connection.commit()
connection.close()
