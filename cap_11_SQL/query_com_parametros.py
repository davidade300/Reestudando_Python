import sqlite3
from contextlib import closing

nome: str = input("digite um nome a consultar")

with sqlite3.connect("agenda.db") as conn:
    with closing(conn.cursor()) as cursor:
        cursor.execute("SELECT * FROM agenda WHERE nome = ?", (nome,))
        # o segundo parametro de execute é uma tupla e tuplas,
        # mesmo que de 1 só item, são escritas com uma virgula
        x: int = 0

        while True:
            resultado = cursor.fetchone()

            if resultado is None:
                if x == 0:
                    print("Nada encontrado.")
                break

            print(f"Nome: {resultado[0]}\nTelefone: {resultado[1]}")
            x += 1
