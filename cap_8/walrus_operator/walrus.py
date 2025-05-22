### Exemplo sem o walrus operator ###

soma = 0.0
valor = input("Digite fim para temrinar ou um número para somar: ")

while valor != "fim":
    soma += float(valor)
    valor = input("Digite fim para terminar ou um número para somar")

print(f"A soma é: {soma}")

### Exemplo com o walrus operator ###

soma = 0.0
while (
    valor := input("Digite fim para terminar ou um número para somar: ")
) != "fim":
    soma += float(valor)

print(f"A soma é {soma}")
