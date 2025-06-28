import sqlite3
from contextlib import (
    closing,  # -> automaticamente fecha algo ao final de um bloco
)

with sqlite3.connect("agenda.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute("SELECT * FROM agenda")

        while True:
            resultado = cursor.fetchone()

            if resultado is None:
                break

            print(f"Nome: {resultado[0]}\nTelefone: {resultado[1]}\n{'=' * 30}")
