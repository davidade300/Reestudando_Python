import sqlite3
from contextlib import closing

with sqlite3.connect("agenda.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute("UPDATE agenda SET telefone = '8876-5432'")

        print(f"Registros alterados: {cursor.rowcount}")

        if cursor.rowcount == 1:
            conexao.commit()
            print("Alteracoes gravadas")
        else:
            conexao.rollback()
            print("Alterações abortadas")
