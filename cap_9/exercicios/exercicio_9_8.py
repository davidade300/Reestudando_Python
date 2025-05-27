import os
import sys

# LARGURA = 76
# LINHAS = 60

LARGURA = int(sys.argv[1])
LINHAS = int(sys.argv[2])


entrada = open(
    f"{os.getcwd()}/python_nilo_4ed/cap_9/processamento_de_arquivos/entrada_2.txt",
    encoding="utf-8",
)

saida = open(
    f"{os.getcwd()}/python_nilo_4ed/cap_9/processamento_de_arquivos/saida.txt",
    "w",
    encoding="utf-8",
)

NOME_ARQUIVO = "lorem_ipsum.txt"


def verifica_pagina(arquivo, linha, pagina):
    if linha == LINHAS:
        rodape = f"{NOME_ARQUIVO} - Pagina: {pagina} ="
        arquivo.write(rodape.center(LARGURA - 1) + "\n")
        pagina += 1
        linha = 1

    return linha, pagina


def escreve(arquivo, linha, nlinhas, pagina):
    arquivo.write(linha + "\n")

    return verifica_pagina(arquivo, nlinhas + 1, pagina)


pagina = 1
linhas = 1

for linha in entrada.readlines():
    palavras = linha.rstrip().split()
    linha = ""

    for p in palavras:
        p = p.strip()

        if len(linha) + len(p) + 1 > LARGURA:
            linhas, pagina = escreve(saida, linha, linhas, pagina)
            linha = ""

        linha += p + " "

    if linha != "":
        linha, pagina = escreve(saida, linha, linhas, pagina)

while linhas != 1:
    linhas, pagina = escreve(saida, "", linhas, pagina)

entrada.close()
saida.close()
