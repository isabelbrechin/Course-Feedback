import sqlite3

connection = sqlite3.connect('database.db')

cur = connection.cursor()

with open('schema.sql') as f:
    script = f.read()
    cur.executescript(script)

cur.execute("INSERT INTO researcher (ResearcherName, ResearcherEmail) VALUES (?, ?)", ('Test Researcher', 'Test.Researcher@dal.ca'))
cur.execute("INSERT INTO prompts (ResearcherID, Consent, Msg) VALUES (?, ?, ?)", (1, 'This is my test form. It is great!', 'This is a test response. It is not as great as you thought.'))


connection.commit()
connection.close()