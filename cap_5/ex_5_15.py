# Controle de máquina registradora

acumulador_total: float = 0
preco: float = 0

while True:
    codigo = int(
        input(
            "digite o código do produto: \
            \n 1 - 0,5\
            \n 2 - 1,00\
            \n 3 - 4,00\
            \n 5 - 7,00\
            \n 9 - 8,00\
            \n 0 para sair"
        )
    )

    if codigo == 0:
        break

    qtd_comprada = int(input("digite a quantidade comprada: "))

    if codigo == 1:
        preco = 0.50

    if codigo == 2:
        preco = 1.00

    if codigo == 3:
        preco = 4.00

    if codigo == 5:
        preco = 7.00

    if codigo == 9:
        preco = 8.00

    acumulador_total += qtd_comprada * preco

print(f"total: {acumulador_total:8.4f}")
