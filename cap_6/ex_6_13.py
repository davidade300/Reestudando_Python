lista: list = [-10, -8, 0, 1, 2, 5, -2, -4]

maximo = lista[0]
minimo = lista[0]

for indice in lista:
    if indice > maximo:
        maximo = indice

    if indice < minimo:
        minimo = indice

print(f"maximo: {maximo} | minimo: {minimo}")
