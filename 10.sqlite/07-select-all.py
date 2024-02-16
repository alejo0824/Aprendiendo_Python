import sqlite3

with sqlite3.connect("10.sqlite/app.db") as con:
    cursor = con.cursor()
    cursor.execute("SELECT * FROM usuarios")
    print(cursor.fetchall())
