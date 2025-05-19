# Generator capaz de gerar uma sequência com o fatorial de 1 até n,
# n é passado como parâmetro para o gerador.


from typing import Any


def fatorial(n) -> Any:
    p = 1

    for x in range(1, n + 1):
        p *= x

        yield p


for n, fatorial in enumerate(fatorial(5), 1):
    print(f"{n}! = {fatorial}")
