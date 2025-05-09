# Programa 6.13: Controle de utilização de salas de um cinema
# A lista "lugares_vagos" contém o numero de lugares vagos nas salas 1,2,3,4 e 5
# respectivamente

import time  # noqa: F401

lugares_vagos: list = [10, 2, 1, 3, 0]

while True:
    sala = int(input("sala (0 sai): "))

    if sala == 0:
        print("fim")
        break

    if sala > len(lugares_vagos) or sala < 1:
        print("sala invalida")

    elif lugares_vagos[sala - 1] == 0:
        print("desculpe, sala lotada")

    else:
        lugares = int(
            input(
                f"Quantos lugares voce deseja ({lugares_vagos[sala - 1]} vagos): "
            )
        )

        if lugares > lugares_vagos[sala - 1]:
            print("Esse numero de lugares não está disponível. ")
        elif lugares < 0:
            print("numero invalido")
        else:
            lugares_vagos[sala - 1] -= lugares
            print(f"{lugares} lugares vendidos")

print("Utilização das salas")

for sala, vagos in enumerate(lugares_vagos):
    print(f"Sala {sala + 1} - {vagos} lugar(es) vazio(s)")
a: str = "a"


def funcao(a, b):
    a += 1
    b += 2


class Pessoa(object):
    def __init__(self) -> None:
        pass
