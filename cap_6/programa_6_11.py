# Programa 6.11: Verificação do maior valor

lista: list = [1, 7, 2, 4]
maximo = lista[0]

for indice in lista:
    if indice > maximo:
        maximo = indice

print(maximo)
