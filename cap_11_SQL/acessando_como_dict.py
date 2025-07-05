import sqlite3
from contextlib import closing

conexao = sqlite3.connect("agenda.db")

conexao.row_factory = sqlite3.Row  # permite acessar campos por posicao

with closing(conexao.cursor()) as cursor:
    for registro in cursor.execute("SELECT * FROM agenda"):
        print(f"Nome: {registro['nome']}\nTelefone: {registro['telefone']}")

        #

# for registro in conexao.execute("SELECT * FROM agenda"):
# print(f"Nome: {registro['nome']}\nTelefone: {registro['telefone']}")


# cursor.close()
# conexao.close()
