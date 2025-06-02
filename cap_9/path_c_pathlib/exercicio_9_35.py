# Exercicio 9.35: criando pagina html com o nome e tamanho de cada
# arquivo de um diretorio passado e seus subdiretórios

import os
import os.path
import sys
import urllib.request

style_mask = "'margin: 5px 0px 5px %dpx;'"


def gera_estilo(nivel):
    return style_mask % (nivel * 20)


def gera_listagem(pagina, diretorio):
    nraiz = os.path.abspath(diretorio).count(os.sep)

    for raiz, diretorios, arquivos in os.walk(diretorio):
        nivel = raiz.count(os.sep) - nraiz

        pagina.write(f"<p style={gera_estilo(nivel)}>{raiz}</p>")

        estilo = gera_estilo(nivel + 1)

        for a in arquivos:
            caminho_completo = os.path.join(raiz, a)

            tamanho = os.path.getsize(caminho_completo)
            link = urllib.request.pathname2url(caminho_completo)

            pagina.write(
                f"<p style={estilo}><a href='{link}'>{a}</a> ({tamanho} bytes)</p>"
            )


if len(sys.argv) < 2:
    print("Digite o nome do diretorio para coletar os arquivos!")
    sys.exit(1)

diretorio = sys.argv[1]

pagina = open("arquivos.html", "w", encoding="utf-8")

pagina.write("""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Arquivos</title>
</head>
<body>
""")

pagina.write(f"Arquivos encontrados a partir do diretório: {diretorio}")

gera_listagem(pagina, diretorio)

pagina.write("""
</body>
</html>
""")

pagina.close()
