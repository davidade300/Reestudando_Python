# Obtenção de preço com um dicionario

tabela = {
    "alface": 0.45,
    "batata": 1.20,
    "tomate": 2.30,
    "feijao": 1.50,
}
while True:
    produto = input("Digite o nome do produto, fim para terminar: ")

    if produto == "fim":
        break

    if produto in tabela:
        print(f"Preço {tabela[produto]:5.2f}")  # tabela na chave produto
    else:
        print("Produto não encontrado")
