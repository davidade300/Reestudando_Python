# fatorial


def fatorial(
    valor: int,
):
    resultado: int = 1

    if valor == 0:
        return resultado

    while valor > 1:
        resultado *= valor
        valor -= 1

    return resultado


print(fatorial(4))
