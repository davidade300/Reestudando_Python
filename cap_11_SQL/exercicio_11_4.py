import sqlite3

nome: str = input("digite o nome do produto a consultar: ")
preco: float = float(input("digite o preco do produto a consultar: "))

conn: sqlite3.Connection = sqlite3.connect("precos.db")
cursor: sqlite3.Cursor = conn.cursor()

cursor.execute(
    "SELECT * FROM precos WHERE nome = ? AND preco = ?", (nome, preco)
)

x: int = 0

while True:
    resultado = cursor.fetchone()

    if resultado is None:
        if not x:
            print("nada encontrado.")
        break

    print(f"Nome: {resultado[0]}\nPreco: {resultado[1]}")

    x += 1

cursor.close()
conn.close()
