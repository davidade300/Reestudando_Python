# Exercicio 8.22: Programa 8.28 adicionado de raiz quadrada e potenciacao

import math
import operator
from functools import partial


def executa(operacao, simbolo, *args):
    resultado = operacao(*args)

    if operacao in ["+", "-", "*", "/"]:
        print(f"{args[0]} {simbolo} {args[1]} = {resultado}")
    else:
        print(f"{args[0]} {simbolo} = {resultado}")


operacoes = {
    "+": partial(executa, operator.add, "+"),
    "-": partial(executa, operator.sub, "-"),
    "*": partial(executa, operator.mul, "*"),
    "/": partial(executa, operator.truediv, "/"),
    "**": partial(executa, operator.pow, "**"),
    "**1/2": partial(executa, math.sqrt, "**1/2"),
}

operacao = input("digite o simbolo da operacao desejada: ").strip()
operandos = []
contador = 1

if operacao == "**1/2":
    operandos.append(float(input("Digite o operando: ")))
else:
    while contador <= 2:
        operandos.append(float(input(f"Digite o operando {contador}: ")))
        contador += 1

if operacao in operacoes:
    operacoes[operacao](*operandos)
else:
    print("operacao invalida")
