# Programa 9.8: geração de uma pagina web a partir de um dicionario

filmes: dict = {
    "drama": ["Cidadao Kane", "O poderoso chefao"],
    "comedia": ["Tempos modernos", "American Pie", "Dr Dolittle"],
    "policial": ["Chuva negra", "Desejo de matar", "dificil de matar"],
    "guerra": ["Rambo", "Platoon", "tora!tora!tora!"],
}

with open("filmes.html", "w", encoding="utf-8") as pagina:
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

    for k, v in filmes.items():
        pagina.write(f"<h1>{k}</h1>\n")
        for e in v:
            pagina.write(f"<h2>{e}</h2>\n")

    pagina.write("""</body>
</html>""")
