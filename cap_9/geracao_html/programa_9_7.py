# Programa 9.7: criacao de pagina inicial html em python

with open("pagina.html", "w", encoding="utf-8") as pagina:
    pagina.write("<!DOCTYPE html>\n")
    pagina.write('<html lang="pt-BR">\n')
    pagina.write("<head>\n")
    pagina.write('<meta charset="UTF-8">\n')
    pagina.write(
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
    )
    pagina.write("<title>Document</title>\n")
    pagina.write("</head>\n")
    pagina.write("<body>\n")
    pagina.write("    olá\n")
    for linha in range(10):
        pagina.write(f"<p>{linha}</p>\n")
    pagina.write("</body>\n")
    pagina.write("</html>")
