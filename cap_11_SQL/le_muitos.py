import sqlite3

conexao = sqlite3.connect("agenda.db")
cursor = conexao.cursor()

cursor.execute("SELECT * FROM agenda")
resultado = (
    cursor.fetchall()
)  # 1 -> retorna uma lista de tuplas com os resultados da consulta

for registro in resultado:
    print(
        f"{'=' * 30}\nNome: {registro[0]}\nTelefone: {registro[1]}\n{'=' * 30}"
    )

cursor.close()
conexao.close()
