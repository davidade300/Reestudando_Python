# Programa 11.2
import sqlite3

conexao = sqlite3.connect("agenda.db")
cursor = conexao.cursor()

cursor.execute("SELECT * FROM agenda")

while True:
    resultado = cursor.fetchone()

    if resultado is None:
        print("FIM DOS REGISTROS")
        break

    print(f"Nome: {resultado[0]}\nTelefone: {resultado[1]}\n{'=' * 30}")

cursor.close()
conexao.close()
