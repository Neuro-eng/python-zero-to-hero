import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE todos (id INTEGER PRIMARY KEY, title TEXT, done INTEGER DEFAULT 0)")
conn.executemany("INSERT INTO todos (title) VALUES (?)", [("Learn SQL",), ("Build API",)])
for row in conn.execute("SELECT id, title, done FROM todos"):
    print(row)
conn.close()
