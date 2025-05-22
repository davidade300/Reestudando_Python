# Programa 8.28: Usando partial com as operacoes
# ver programa 8.27 em caso de dúvida

import operator
from functools import partial


def executa(operacao, simbolo, operando_1, operando_2):
    resultado = operacao(float(operando_1), float(operando_2))

    print(f"{operando_1} {simbolo} {operando_2} = {resultado}")


operacoes = {
    "+": partial(executa, operator.add, "+"),
    "-": partial(executa, operator.sub, "-"),
    "*": partial(executa, operator.mul, "*"),
    "/": partial(executa, operator.truediv, "/"),
}

operando_1 = input("operador 1: ")
operando_2 = input("operador 2: ")
operacao = input("Operacao : ").strip()

if operacao in operacoes:
    operacoes[operacao](operando_1, operando_2)
else:
    print("operacao invalida")
