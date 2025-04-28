# Programa que aceita uma string como entrada e imprime quantas vogais ela contém.
# O programa não leva em consideração se caixa alta ou baixa

frase: str = input("Digite o seu texto para a contagem de vogais: ")
vogais: str = "aeiou"


### contador ###

for vogal in vogais:
    contador = frase.lower().count(vogal)
    if contador > 0:
        print(f"{vogal}: {contador}")

### solução inicial ###
"""
frase: str = input("Digite o seu texto para a contagem de vogais: ")
vogais: dict = {
    "a": 0,
    "e": 0,
    "i": 0,
    "o": 0,
    "u": 0,
}

for letra in frase.lower():
    if letra in vogais:
        vogais[letra] += 1

"""

### Solução do autor ###
"""
vogais: str = "aeiou"
frase = input("Digite uma frase: ")
frase_minúscula = frase.lower()
for vogal in vogais:
    ocorrência_vogal = frase_minúscula.count(vogal)
    if ocorrência_vogal > 0:
        print(f"{vogal} aparece {ocorrência_vogal} vez(es)")"""
