import sqlite3

conn = sqlite3.connect("precos.db")
cursor = conn.cursor()


values: list[tuple[str, float]] = [
    ("produto_1", 9.10),
    ("produto_2", 10.9),
    ("produto_3", 91.0),
]
cursor.execute("CREATE TABLE precos (nome TEXT, preco FLOAT)")
cursor.executemany("INSERT INTO precos(nome, preco) VALUES (?,?)", values)

conn.commit()
cursor.close()
conn.close()
