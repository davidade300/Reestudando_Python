import sqlite3

print("Região Estados População  Mínima    Máxima      Média    Total (soma)")
print("====== =======          ========= ========== ==========  ============")

with sqlite3.connect("brasil.db") as conexao:
    for regiao in conexao.execute(
        "SELECT regiao, COUNT(*), MIN(populacao), MAX(populacao), AVG(populacao),SUM(POPULACAO) FROM estados GROUP BY regiao ORDER BY SUM(populacao) DESC;"
    ):
        print("{0:6} {1:7} {2:18,} {3:10,} {4:10,.0f} {5:13,}".format(*regiao))

    print(
        "\nBrasil: {0:6} {1:18,} {2:10,} {3:10,.0f} {4:13,}".format(
            *conexao.execute(
                "SELECT COUNT(*), MIN(populacao), MAX(populacao), AVG(populacao), SUM(POPULACAO) FROM estados"
            ).fetchone()
        )
    )
