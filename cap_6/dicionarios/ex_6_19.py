# Exemplo de um dicionario com estoque e operações de venda

estoque: dict = {
    "tomate": [1000, 2.30],
    "alface": [500, 0.45],
    "batata": [2001, 1.20],
    "feijao": [100, 1.50],
}

total: float = 0
custo: float = 0

while True:
    produto: str = input('Digite o nome do produto ("fim" para sair)')

    if produto == "fim":
        break

    if produto not in estoque:
        print(
            "Produto não disponível, produtos disponíveis: tomate, alface, batata, feijao"
        )

    if produto in estoque:
        quantidade: int = int(input("Digite a quantidade vendida:"))

        if quantidade <= estoque[produto][0]:
            estoque[produto][0] -= quantidade
            total += quantidade * estoque[produto][1]
            print(
                f"{produto:12s}: {quantidade:3d} x {estoque[produto][1]:6.2f} = {total:6.2f}"
            )
        else:
            print(
                f"Quantidade não disponivel, estoque total para {produto} : {estoque[produto][0]}"
            )

        custo += total


for chave, dados in estoque.items():
    print("Descricao: ", chave)
    print("Quantidade: ", dados[0])
    print(f"Preço: {dados[1]:6.2f}\n")
