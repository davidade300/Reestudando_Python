import sqlite3
from contextlib import closing

with sqlite3.connect("agenda.db") as conn:
    with closing(conn.cursor()) as cursor:
        cursor.execute("SELECT * FROM agenda WHERE nome = 'David'")
        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                break

            print(f"Nome: {resultado[0]}\nTelefone: {resultado[1]}")
