# Exemplo de um dicionario com estoque e operações de venda

estoque: dict = {
    "tomate": [1000, 2.30],
    "alface": [500, 0.45],
    "batata": [2001, 1.20],
    "feijao": [100, 1.50],
}

venda: list[list] = [["tomate", 5], ["batata", 10], ["alface", 5]]
total: int = 0

print("Vendas:\n")

for operacao in venda:
    produto, quantidade = operacao  # 1
    # 1: desempacotamento, como operacao é uma lista com 2 elementos, o primeiro
    # elemento de operacao é atribuido a produto e o segundo a quantidade
    preco = estoque[produto][1]
    custo = preco * quantidade

    print(f"{produto:12s}: {quantidade:3d} x {preco:6.2f} = {custo:6.2f}")

    estoque[produto][0] -= quantidade
    total += custo

print(f"Custo total: {total:21.2f}\n")
print("Estoque:\n")

for chave, dados in estoque.items():
    print("Descricao: ", chave)
    print("Quantidade: ", dados[0])
    print(f"Preço: {dados[1]:6.2f}\n")
