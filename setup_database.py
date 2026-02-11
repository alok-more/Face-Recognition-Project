import sqlite3

conn = sqlite3.connect("database.db")
conn.execute('''CREATE TABLE IF NOT EXISTS student
             (ID INTEGER PRIMARY KEY,
              Name TEXT NOT NULL,
              Age INTEGER NOT NULL);''')
conn.commit()
conn.close()
