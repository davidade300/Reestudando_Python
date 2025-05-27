# Exercicio 9.10: programa que recebe uma lista de nome de arqs e os escreve em 1 arq de saida

import sys

if len(sys.argv) < 2:
    print("\n uso: exercicio_9_10.py arquivo1 arquivo2 ... arquivon \n")
    sys.exit()

with open("saida.txt", "w") as file:
    for nome in sys.argv[1:]:
        arquivo = open(nome, "r")

        for linha in arquivo:
            file.write(linha)

        arquivo.close()
