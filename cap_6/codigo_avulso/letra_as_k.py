palavra: str = input("digite o texto para avaliação")

dicionario: dict = {}

for letra in palavra:
    if letra == " ":
        pass
    if letra in dicionario:
        dicionario[letra] += 1
    if letra not in dicionario:
        dicionario[letra] = 1

print(dicionario)
