# Programa 9.16: Abrindo um json e usando os dados

import json
from pathlib import Path

with Path("python_nilo_4ed/cap_9/arqs_json/lista.json").open(
    encoding="utf-8"
) as arquivo:
    turma = json.load(arquivo)

for aluno in turma:
    print("Nome:", aluno["nome"])
    print("Notas:", aluno["notas"])
    print("Media:", sum(aluno["notas"]) / len(aluno["notas"]))
    print()
