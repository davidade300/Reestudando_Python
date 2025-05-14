# Programas:
#   8.25: Navegando listas a partir do tipo de seus elementos
#   8.26: Imprimindo uma lista de inteiros com múltiplos niveis

#: 8.25

L: list = ["a", ["b", "c", "d"], "e"]

for x in L:
    if isinstance(x, str):
        print(x)
    else:
        print("Lista: ", end="")
        for z in x:
            print(f" {z}", end="")
        print()

#: 8.26


def imprime_lista(lista, nivel=0):
    for x in lista:
        if isinstance(x, int):
            print(f"{x:{nivel * 2}}")  # por padrão o padding é a esquerda
        else:
            imprime_lista(x, nivel + 1)


imprime_lista([1, [2, 3, 4], [5, 6, [7, 8, 9]], 10])
