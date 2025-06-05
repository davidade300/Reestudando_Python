# Execicio 9.38: ex 9.37 modificado para ler o mesmo arquivo, permitindo
# adicionar mais dados ao arquivo. Se o mesmo nome for digitado duas vezes
# altera os dados para a nova entrada

import json
import os


def ler_notas():
    notas = []

    for i in range(4):
        nota = float(input(f"Digite a {i + 1}º nota: "))
        notas.append(nota)

    return notas


def carregar_dados():
    if not os.path.exists("aluno_notas.json"):
        return []

    try:
        with open("alunos_notas.json", "r") as arquivo:
            return json.load(arquivo)

    except json.JSONDecodeError:
        return []


# lê dados já existentes
alunos = carregar_dados()

# leitura de novos dados
nome = input("Digite o nome do aluno: ")
notas = ler_notas()

# Criacao do dicionário com os novos dados
novo_aluno = {"nome": nome, "notas": notas}

aluno_existente = False

for i, aluno in enumerate(alunos):
    if aluno["nome"] == nome:
        alunos[i] = novo_aluno
        aluno_existente = True

        break

if not aluno_existente:
    alunos.append(novo_aluno)


with open("alunos_nota.json", "w") as arquivo:
    json.dump(alunos, arquivo, indent=4)
