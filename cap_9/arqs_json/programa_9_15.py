# Programa 9.15: Lendo um arquivo JSON

import json
from pathlib import Path

with Path("python_nilo_4ed/cap_9/arqs_json/dados.json").open() as arquivo:
    dados = json.load(arquivo)

print(dados["nome"])
print(dados["valores"])
