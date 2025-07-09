import sqlite3

with sqlite3.connect(
    "brasil.db", detect_types=sqlite3.PARSE_DECLTYPES
) as conexão:
    conexão.row_factory = sqlite3.Row
    for feriado in conexão.execute("select * from feriados"):
        print(f"{feriado['data'].strftime('%d/%m')} {feriado['descrição']}")
