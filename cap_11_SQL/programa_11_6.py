import sqlite3
from contextlib import closing

with sqlite3.connect("agenda.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute("UPDATE agenda SET telefone = '9876-5432'")

        print(f"Registros alterados: {cursor.rowcount}")
