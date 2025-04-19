# Programa 6.2 calculo da media com notas digitadas

notas: list = [0, 0, 0, 0, 0, 0, 0]
soma = 0
x = 0

while x < 5:
    notas[x] = float(input(f"notas {x}: "))
    notas += notas[x]

    x += 1

x = 0

while x < 5:
    print(f"nota {x}: {notas[x]:6.2f}")

print(f"Média: {soma / x:5.2f}")
