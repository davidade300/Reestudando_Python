# Reescrição do programa 8.1 usando funções de pesquisa em lista


def pesquisa(lista: list, valor: int):
    if valor in lista:
        return lista.index(valor)

    return None


L = [10, 20, 25, 30]

print(pesquisa(L, 25))
print(pesquisa(L, 27))
