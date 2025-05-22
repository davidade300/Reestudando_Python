# Programa que recebe o nome de um arquivo pelo terminl e imprime todas as linhas desse arquivo

import sys

arquivo = sys.argv[1]  # o primerio argumento é o nome do programa

with open(arquivo, "r") as file:
    for line in file.readlines():
        print(line)
