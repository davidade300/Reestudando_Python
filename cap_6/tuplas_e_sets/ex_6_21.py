"""
Programa para comparação de duas listas usando operações com sets(conjuntos)
O programa imprime:
    - Os valores comums às duas listas;
    - Os valores que existem apenas na primeira lista;
    - Os valores que existem apenas na segunda lista;
    - Uma lista com os elementos não repetidos das duas listas;
    - a primeira lista sem os elementos repetidos na segunda
"""

lista_1: list = [1, 2, 3, 4, 5, 6]
lista_2: list = [4, 5, 6, 7, 8, 9]

print(
    "elementos comums: " + str(set(lista_1) & set(lista_2))
)  # elementos comuns (interseção)

print(
    "valores existentes apenas na primeira lista: "
    + str(
        set(lista_1) - set(lista_2)
    )  # elementos que existem apenas na primeira lista
)

print(
    "valores existentes apenas na primeira lista: "
    + str(
        set(lista_2) - set(lista_1)
    )  # elementos que existem apenas na segunda lista
)

print(
    "elementos não repetidos: " + str(set(lista_1) ^ set(lista_2))
)  # elementos não repetidos (diferença simetrica)

print(
    "elementos não repetidos: " + str(set(lista_1) - set(lista_2))
)  # a primeira lista sem os elementos repetidos na segunda
