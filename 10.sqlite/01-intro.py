# Para trabajar con SQLite en Python, puedes utilizar el módulo incorporado sqlite3
import sqlite3

# Conectarse a la base de datos (se crea si no existe)
con = sqlite3.connect("10.sqlite/app.db")

# Cerrar conexión (Siempre hay qu cerrarla)
con.close()
