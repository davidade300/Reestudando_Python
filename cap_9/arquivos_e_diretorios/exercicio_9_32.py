# Programa 9.9 modificado para receber o nome do arquivo ou diretorio pela linha de comando.
# imprime se for um arquivo ou dir e se existir

import os
import sys

if os.path.exists(sys.argv[1]):
    print(f"Arquivo {sys.argv[1]} existe")

if os.path.isfile(sys.argv[1]):
    with open(sys.argv[1], "r", encoding="utf-8") as arq:
        for line in arq.readlines():
            print(line)
