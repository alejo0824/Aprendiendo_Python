import sqlite3

# Forma pas insertar multiples líneas a una tabla SQL

with sqlite3.connect("10.sqlite/app.db") as con:
    cursor = con.cursor()
    usuarios = [
        (2, "Chanchito Feliz"),
        (3, "Chanchito triste"),
    ]
    cursor.executemany(
        # Para prevenir SQL injection usamos los ??
        " INSERT INTO usuarios values(?,?)",
        usuarios
    )
