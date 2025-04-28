# Programa que lê uma string e imprime quantas vezes cada caractere aparece nela

texto: str = "TTAAC"

contador: dict = {}

for letra in texto:
    if letra in contador:
        contador[letra] += 1
    else:
        contador[letra] = 1

print(
    f"String:    {texto}\
    \nResultado:"
)
for chave, valor in contador.items():
    print(f"{chave}: {valor:>12}x")
