# Programa que conta todas as palavras de uma frase

frase: str = input("digite a sua frase:")

palavras: list = frase.split(sep=" ")

print(f"Quantidade de palavras: {len(palavras)}")
