# Programa 8.15: Funcao soma com numero indeterminado de parametros


def soma(*args):
    s = 0
    for arg in args:
        s += arg
    return s


print(soma(1, 2))
print(soma(2))
print(soma(5, 6, 7, 8))
print(soma())
