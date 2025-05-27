# Exercicio 9.9: programa que recebe uma lista de nome de arqs e os imprime

import sys

if len(sys.argv) < 2:
    print("\n uso: exercicio_9_9.py arquivo1 arquivo2 ... arquivon \n")
    sys.exit()


for nome in sys.argv[1:]:
    arquivo = open(nome, "r")

    for linha in arquivo:
        print(linha, end="")

    arquivo.close()
