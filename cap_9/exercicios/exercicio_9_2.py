# Ex 9.1 modificado para receber mais 2 parametros: linha de inicio e de fim
# para impressão

import sys

arquivo = sys.argv[1]  # o primerio argumento é o nome do programa
linha_inicial = int(sys.argv[2])
linha_final = int(sys.argv[3])

with open(arquivo, "r") as file:
    for line in file.readlines()[linha_inicial - 1 : linha_final]:
        # o método readlines gera uma lista em que cada elemento é uma linha
        # do arquivo
        print(line[:-1])
