# Função soma com parametros opcionais


def soma(a, b, imprime=False):
    s = a + b

    if imprime:
        print(s)

    return s


soma(2, 3)
soma(3, 4, True)
