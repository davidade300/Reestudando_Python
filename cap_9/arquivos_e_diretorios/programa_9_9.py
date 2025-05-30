# Programa 9.9: Verificação se um diretorio ou arquivo já existe

import os.path

if os.path.exists("z"):
    print("O diretorio z existe")
else:
    print("O diretorio z não existe")
