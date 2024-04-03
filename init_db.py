import sqlite3

connection = sqlite3.connect('database.db')

cur = connection.cursor()

with open('schema.sql') as f:
    script = f.read()
    cur.executescript(script)

cur.execute("INSERT INTO feedback (content) VALUES (?)", ('This is a sample piece of feedback',))
cur.execute("INSERT INTO analysis (sentiment, keywords, summary) VALUES (?, ?, ?)", ('postitive', 'keywordkeyword', 'This feedback is generally posisitive, here is a summary.'))

connection.commit()
connection.close()