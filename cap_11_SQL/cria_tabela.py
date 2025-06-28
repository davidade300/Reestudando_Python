import sqlite3  # 1

conexao = sqlite3.connect("agenda.db")  # 2
cursor = conexao.cursor()  # 3 -> cursor é um objeto criado para enviar
# comandos e receber resultados do banco de dados

cursor.execute("CREATE TABLE agenda(nome text, telefone text)")  # 4

cursor.execute(
    "INSERT INTO agenda(nome, telefone) VALUES(?,?)", ("David", "7788-1432")
)  # 5 -> os valores são passados como uma tupla (named, tuple será que funciona? ideia p mais pra frente)

conexao.commit()  # 6 ->"comita" a transacao
cursor.close()  # 7
conexao.close()  # 8
