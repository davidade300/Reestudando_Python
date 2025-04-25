# Programa que gera dicionario em que cada chave seja um caracteres e
# seu valor seja o número desse caractere encontrado em uma frase lida

frase: str = "O rato"
d: dict = {}

for letra in frase:
    if letra in d:
        d[letra] += d[letra] + 1
    else:
        d[letra] = 1
print(d)

print("\nSolução alternativa usando metodo de dicionarios .get()\n")
# solução usando o método get #

d_2: dict = {}

for letra in frase:
    d_2[letra] = d_2.get(letra, 0) + 1

print(d_2)
