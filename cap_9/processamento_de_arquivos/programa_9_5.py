# Programa 9.5: Processamento de um arquivo
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

        else:
            print(linha)
