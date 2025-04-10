"""
Programa para calculo de aumento de salário de funcionário.
Para salário superiores a 1.250, calcula-se um aumento de 10%,
para os inferiories ou giauis, de 15%.
"""

salario = float(input("digite o valor do salário"))

aumento = salario * 0.15

if salario > 1.250:
    aumento = salario * 0.1


print(
    f" salario: R${salario},\n aumento: R${aumento}\n novo salario: R${salario + aumento}"
)
