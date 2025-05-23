# Programa que recebe o nome de dois arquivos como parametro na linha de comando e
# gera um arquivo de saída com as linhas do primeiro arquivo seguido das linhas do
# segundo, o nome do arq de saida tambem pode ser passado como parametro na linha
# de comando

import sys

if len(sys.argv) > 4:
    raise Exception("quantiade de argumentos excedeu 4")

file_1 = open(sys.argv[1], "r")
file_2 = open(sys.argv[2], "r")

# print(sys.argv)
# print(len(sys.argv))

if len(sys.argv) == 4:
    file_3 = open(sys.argv[3], "w")

    file_3.writelines(file_1)
    file_3.writelines(file_2)

    file_3.close()


file_1.close()
file_2.close()
