import sqlite3

dados: list[list[str]] = [
    ["SP", "SE", "São Paulo"],
    ["MG", "SE", "Minas Gerais"],
    ["RJ", "SE", "Rio de Janeiro"],
    ["BA", "NE", "Bahia"],
    ["RS", "S", "Rio Grande do Sul"],
    ["PR", "S", "Paraná"],
    ["PE", "NE", "Pernambuco"],
    ["CE", "NE", "Ceará"],
    ["PA", "N", "Pará"],
    ["MA", "NE", "Maranhão"],
    ["SC", "S", "Santa Catarina"],
    ["GO", "CO", "Goiás"],
    ["PB", "NE", "Paraíba"],
    ["ES", "SE", "Espírito Santo"],
    ["AM", "N", "Amazonas"],
    ["RN", "NE", "Rio Grande do Norte"],
    ["AL", "NE", "Alagoas"],
    ["PI", "NE", "Piauí"],
    ["MT", "CO", "Mato Grosso"],
    ["DF", "CO", "Distrito Federal"],
    ["MS", "CO", "Mato Grosso do Sul"],
    ["SE", "NE", "Sergipe"],
    ["RO", "N", "Rondônia"],
    ["TO", "N", "Tocantins"],
    ["AC", "N", "Acre"],
    ["AP", "N", "Amapá"],
    ["RR", "N", "Roraima"],
]

conexao: sqlite3.Connection = sqlite3.connect("brasil.db")
cursor: sqlite3.Cursor = conexao.cursor()

cursor.execute("ALTER TABLE estados ADD sigla TEXT")
cursor.execute("ALTER TABLE estados ADD regiao TEXT")

cursor.executemany(
    "UPDATE estados SET sigla = ?, regiao = ? WHERE nome = ? ;", dados
)

conexao.commit()

cursor.close()
conexao.close()
