import sqlite3

connection = sqlite3.connect('database.db')

cur = connection.cursor()

with open('schema.sql') as f:
    script = f.read()
    cur.executescript(script)

cur.execute("INSERT INTO feedback (content) VALUES (?)", ('This is a sample piece of feedback',))
cur.execute("INSERT INTO analysis (sentiment, keywords, summary, recommended_actions) VALUES (?, ?, ?, ?)",
              ('Positive', 'participation, engagement', 'The feedback is generally positive, with suggestions for more class discussions.', 'Consider incorporating more interactive activities to increase class engagement.'))

connection.commit()
connection.close()