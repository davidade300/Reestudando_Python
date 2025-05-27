# Exercicio 9.6: programa 9.5 modificado para imprimir 40x "=" se for o 1 char da linha
# adiciona tambem a opcaao de parar de imprimir até que enter seja pressionado

import os

LARGURA = 79

# print(f"{os.getcwd()}/entrada.txt")
caminho = (
    f"{os.getcwd()}/python_nilo_4ed/cap_9/processamento_de_arquivos/entrada.txt"
)
with open(caminho) as entrada:
    for linha in entrada.readlines():
        if linha[0] == ";":
            continue

        elif linha[0] == ">":
            print(linha[1:].rjust(LARGURA))

        elif linha[0] == "*":
            print(linha[1:].center(LARGURA))

        elif linha[0] == "=":
            print(40 * linha[0])

        elif linha[0] == ".":
            input("Pressione enter para continuar")
            print()

        else:
            print(linha)
