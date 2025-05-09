# Fatorial escrito de forma recursiva


def fatorial(numero: int):
    if (numero == 0) or (numero == 1):
        return 1

    return numero * fatorial(numero - 1)


print(fatorial(5))
