# Progra 6.13 modificado para mostrar quantos ingressos foram vendidos em cada sala

n_salas = int(input("Quantidade de salas vazias: "))
lugares_vagos: list = []

for sala in range(n_salas):
    lugares_vagos.append(
        int(input(f"Quantidade de lugares vagos há na sala {sala + 1}: "))
    )

vendidos: list = [0] * len(lugares_vagos)

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
            vendidos[sala - 1] += lugares
            print(f"{lugares} lugares vendidos")

print("\nUtilização das salas")

for sala, vagos in enumerate(lugares_vagos):
    print(
        f"Sala {sala + 1} - {vagos} lugar(es) vazio(s) - {vendidos[sala]} lugares vendidos"
    )
print("total de lugares vendidos: " + str(sum(lugares for lugares in vendidos)))
