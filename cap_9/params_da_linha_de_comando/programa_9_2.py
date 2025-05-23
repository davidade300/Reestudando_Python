# Programa 9.2: uso do with

with open("numeros.txt", "r") as file:
    for linha in file.readlines():
        print(linha)
