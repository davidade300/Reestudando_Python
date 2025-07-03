import sqlite3

conn = sqlite3.connect("precos.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM precos")
resultado = cursor.fetchall()

for registro in resultado:
    print(
        f"{'=' * 30}\nNome: {registro[0]}\nTelefone: {registro[1]}\n{'=' * 30}"
    )


cursor.close()
conn.close()
