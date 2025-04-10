dep_inicial = float(input("Digite o valor do depósito inicial: "))
taxa_de_juros = float(input("Digite o valor da taxa de juros de 0.00 a 1.00: "))
valor_mensal = float(input("Digite o valor do depósito mensal: "))
prazo: int = 1
total: float = dep_inicial

while prazo <= 24:
    total += total * taxa_de_juros
    total += valor_mensal
    prazo += 1

    print(f"{total:5.2f}")
