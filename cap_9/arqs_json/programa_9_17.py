# Programa 9.17: Criando uma tabela de preços em formato JSON

import json
from pathlib import Path

tabela_de_precos: dict = {}

print("criador de tabela de precos")
print("Digite um nome de produto em branco para terminar")

while produto := input("nome do produto"):
    preco = input("preco: ")
    tabela_de_precos[produto] = preco

with Path("Precos.json").open("w", encoding="utf-8") as arquivo:
    json.dump(tabela_de_precos, arquivo, indent=2, ensure_ascii=False)
