# Buble sort

# lista: list = [7, 4, 3, 12, 8]
# lista: list = [3, 3, 1, 5, 4]
lista: list = [1, 2, 3, 4, 5]
fim = 5

while fim > 1:
    trocou: bool = False

    x: int = 0

    while x < (fim - 1):
        if lista[x] > lista[x + 1]:
            trocou = True
            temp = lista[x]
            lista[x] = lista[x + 1]
            lista[x + 1] = temp
        x += 1

    if not trocou:
        break

    fim -= 1

for e in lista:
    print(e)
