# Programa 8.2 usando for em vez de while:


def soma(lista: list):
    total: int = 0

    for valor in lista:
        total += valor
    return total


lista_1 = [1, 7, 2, 9, 15]
print(soma(lista_1))
