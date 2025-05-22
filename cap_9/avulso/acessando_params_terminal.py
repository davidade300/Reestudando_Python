"""Podemos acessar parâmetros passados ao programa na linha de comando
utilizando o modulo sys e trabalhando com a lista args"""

# Executar programa a partir do terminal com python acessando_params_terminal.py param_1 param_2 ... param_n

import sys

print(f"numero de parâmetros: {len(sys.argv)}")

for n, p in enumerate(sys.argv):
    print(f"parametro {n} = {p}")
