"""
Identificando o campo data como datetime.date.
Isso evita ter de fazer a conversao manualmente de strin para datetime.date
"""

import sqlite3

with sqlite3.connect(
    "brasil_feriados.db", detect_types=sqlite3.PARSE_DECLTYPES
) as conexao:
    for feriado in conexao.execute("SELECT * FROM feriados;"):
        print(feriado)
