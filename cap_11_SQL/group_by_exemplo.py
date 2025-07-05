import sqlite3

print("Região Número de Estados")
print("====== =================")
with sqlite3.connect("brasil.db") as conexão:
    for regiao in conexão.execute(
        "SELECT regiao, COUNT(*) FROM estados GROUP BY regiao"
    ):
        print(
            "{0:6} {1:17}".format(*regiao)
        )  # posicao 0 de regiao e posicao 1 de regiao
