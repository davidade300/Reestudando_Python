# programa que lê um arquivo-texto e gera um arq de saida paginado.
# Cada linha não deve conter + de 76 chars.
# cada pagina terá no max 60 linhas
# A ultima linha de cada  tera o numero da pagina atual

import os
import typing

entrada = open(
    f"{os.getcwd()}/python_nilo_4ed/cap_9/processamento_de_arquivos/entrada_2.txt",
    "r",
)
saida = open(
    f"{os.getcwd()}/python_nilo_4ed/cap_9/processamento_de_arquivos/saida.txt",
    "w+",
)


def quebra_linhas(entrada: typing.TextIO, saida: typing.TextIO):
    for numero, linha in enumerate(entrada.readlines()):
        contador = numero
        while len(linha) > 76:
            saida.write(linha[0:77] + "\n")
            linha = linha[77:]
            contador += 1
        saida.write(linha)
        if contador % 60 == 0:
            saida.write(f"\n {'*' * 100} \n")


quebra_linhas(entrada, saida)

entrada.close()
saida.close()
