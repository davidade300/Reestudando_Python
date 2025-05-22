# Programa 8.27: Sem usar partial

import operator


def executa(operacao, simbolo, operando_1, operando_2):
    resultado = operacao(float(operando_1), float(operando_2))

    print(f"{operando_1} {simbolo} {operando_2} = {resultado}")


operando_1 = input("Operador 1: ")
operando_2 = input("Operador 2: ")
operacao = input("Operacao: ").strip()

if operacao == "+":
    executa(operator.add, operacao, operando_1, operando_2)
elif operacao == "-":
    executa(operator.sub, operacao, operando_1, operando_2)
elif operacao == "*":
    executa(operator.mul, operacao, operando_1, operando_2)
elif operacao == "/":
    executa(operator.truediv, operacao, operando_1, operando_2)
