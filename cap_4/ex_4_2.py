salario: float = float(input("digite o salario para calculo do imposto: "))

base: float = salario  # 1

imposto: float = 0

if base > 3000:  # 2
    imposto = imposto + ((base - 3000) * 0.35)  # 3
    base = 3000  # 4 # O que ultrapassa 3000 já foi taxado então atualizamos base para 3000

if base > 1000:  # 5
    imposto = imposto + (base - 1000) * 0.20  # 6

# imprime salario e imposto com 6 digitos de tamanho e 2 casas decimais para o console
# imprime teste afastado 12 espaços para a direita
print(
    f" Salario: R${salario:6.2f}\n Imposto a pagar: R${imposto:6.2f}\n teste: R${salario:>12}"
)
