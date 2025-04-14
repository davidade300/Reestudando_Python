valores = [9, 8, 7, 12, 0, 13, 21]
pares = []
ímpares = []
for e in valores:
    if e % 2 == 0:
        pares.append(e)
    else:
        ímpares.append(e)
print("Pares: ", pares)
print("Impares: ", ímpares)
