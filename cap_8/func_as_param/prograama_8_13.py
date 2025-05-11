# Programa 8.13: Funções como parametro


def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def imprime(a, b, foper):
    print(foper(a, b))


imprime(5, 4, soma)
imprime(5, 4, subtracao)
