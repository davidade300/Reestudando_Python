import sqlite3

feriados: list[list[str]] = [
    ["2025-01-01", "Confraternização Universal"],
    ["2025-04-21", "Tiradentes"],
    ["2025-05-01", "Dia do trabalhador"],
    ["2025-09-07", "Independência"],
    ["2025-10-12", "Padroeira do Brasil"],
    ["2025-11-02", "Finados"],
    ["2025-11-15", "Proclamação da República"],
    ["2025-12-25", "Natal"],
]
with sqlite3.connect("brasil_feriados.db") as conexão:
    conexão.execute(
        "create table feriados(id integer primary key autoincrement, data date, descrição text)"
    )
    conexão.executemany(
        "insert into feriados(data,descrição) values (?,?)", feriados
    )
