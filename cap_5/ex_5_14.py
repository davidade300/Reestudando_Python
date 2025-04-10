acumulador_digitados: int = 0
acumulador_soma: int = 0

while True:
    numero = int(input("digite o número (0 para interromper): "))
    if numero == 0:
        break

    acumulador_soma += numero
    acumulador_digitados += 1

print(
    f"total de numeros digitados: {acumulador_digitados} \ntotal da soma: {acumulador_soma}"
)
