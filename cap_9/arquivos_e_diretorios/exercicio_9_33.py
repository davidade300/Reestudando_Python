# Exercicio 9.33: Programa que gera pagina HTML com
# links para todos os arquivos jpg e png encontrados
# a partir de um diretorio informado na linha de comando

import os
import os.path
import sys
import urllib.request

if len(sys.argv) < 2:
    print("Digite o nome do diretorio para coletar os arquivos")
    sys.exit()


diretorio = sys.argv[1]

pagina = open("imagems.html", "w", encoding="utf-8")

pagina.write("""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Document</title>
</head>
<body>
""")

pagina.write(f"Imagens encontradas no diretorio: {diretorio}")

for entrada in os.listdir(diretorio):
    nome, extensao = os.path.splitext(entrada)

    if extensao in [".jpg", "png"]:
        caminho_completo = os.path.join(diretorio, entrada)
        link = urllib.request.pathname2url(caminho_completo)
        pagina.write(f"<p><a href='{link}'>{entrada}</a></p>")

pagina.write("""</body>
</html>""")

pagina.close()
