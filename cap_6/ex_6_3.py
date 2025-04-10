# programa para percorrer duas listas e gerar uma terceira lista sem elementos repetidos

lista_1: list = []
lista_2: list = []
contador: int = 0

while True:
    entrada = int(
        input(f"digite o {contador}º elemento da lista 1 (0 para sair): ")
    )

    if entrada == 0:
        break

    lista_1.append(entrada)

    contador += 1

contador = 0

while True:
    entrada = int(
        input(f"digite o {contador}º elemento da lista 2 (0 para sair): ")
    )

    if entrada == 0:
        break

    lista_2.append(entrada)

    contador += 1

"saida facil"
# lista_final = lista_1[:]
# x: int = 0
# for n in lista_2:
# if n not in lista_final:
# lista_final.append(n)
# print(lista_final)

terceira_lista: list = []
duas_listas = lista_1[:]
duas_listas.extend(lista_2)
x: int = 0

while x < len(duas_listas):
    y: int = 0

    while y < len(terceira_lista):
        if duas_listas[x] == terceira_lista[y]:
            break
        y += 1

    if y == len(terceira_lista):
        terceira_lista.append(duas_listas[x])

    x += 1

x = 0

while x < len(terceira_lista):
    print(f"{x}: {terceira_lista[x]}")

    x += 1
