import sqlite3

with sqlite3.connect("brasil.db") as conn:
    conn.row_factory = sqlite3.Row

    print(f"{'id':3s} {'Estado:':<20s} {'Populacao':12s}")
    print("=" * 37)

    for estado in conn.execute("SELECT * FROM estados ORDER BY nome;"):
        print(
            f"{estado['id']:3d} {estado['nome']:<20s} {estado['populacao']:12d}"
        )
