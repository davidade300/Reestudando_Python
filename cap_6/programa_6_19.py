# Criação e impressão de lista de compras

compras: list = []

while True:
    produto = input("Produto:")

    if produto.casefold() == "fim":
        break

    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço: "))

    compras.append([produto, quantidade, preco])

soma: float = 0.0

for compra in compras:
    print(
        f"{compra[0]:20s} x {compra[1]:5d} {compra[1] * compra[2]:6.2f}"
    )  # :5d -> decimal integer
    # :20s -> string
    # :6.2f -> float de tamanho 6 e 2 casas decimais
