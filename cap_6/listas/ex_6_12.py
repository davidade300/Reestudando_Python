# Exercício 6.12

lista: list = [1, 7, 2, 4]
minimo = lista[0]

for indice in lista:
    if indice < minimo:
        minimo = indice

print(minimo)
