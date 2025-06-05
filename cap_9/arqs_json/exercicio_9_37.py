# Execicio 9.37: Programa que le o nome do alunos e quatro notas, grava os
# dados lidos em um .json em disco

import json
from pathlib import Path

notas: dict = {}

print("registrador de notas.\nDigite uma nota em branco para terminar")

while aluno := input("digite o nome do aluno: "):
    nota = input("nota: ")
    notas[aluno] = nota


with Path("notas.json").open("w", encoding="utf-8") as arquivo:
    json.dump(notas, arquivo, indent=2, ensure_ascii=False)
