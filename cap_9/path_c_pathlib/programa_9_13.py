# Programa 9.13: Arvore de diretorios sendo percorrida com pathlib

import sys
from pathlib import Path

for raiz, diretorios, arquivos in Path(sys.argv[1]).walk():
    print("\nCaminho: ", raiz)

    for d in diretorios:
        print(f"  {d}/")

    for f in arquivos:
        print(f"  {f}")

    print(f"{len(diretorios)} diretorio(s), {len(arquivos)} arquivo(s)")
