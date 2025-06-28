import sqlite3

conexao = sqlite3.connect("agenda.db")
cursor = conexao.cursor()

cursor.execute("SELECT * FROM agenda")  # 1
resultado = (
    cursor.fetchone()
)  # 2 -> retorna uma tupla com os resultados da consulta ou None

print(
    f"{'=' * 30}\nNome: {resultado[0]}\nTelefone: {resultado[1]}\n{'=' * 30}"
)  # 3

cursor.close()
conexao.close()
