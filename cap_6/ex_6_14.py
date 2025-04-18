# Progra 6.13 modificado para mostrar quantos ingressos foram vendidos em cada sala

lugares_vagos: list = [10, 2, 1, 3, 0]
vendidos: list = [0, 0, 0, 0, 0]

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
            vendidos[sala - 1] += lugares
print("Utilização das salas")

for sala, vagos in enumerate(lugares_vagos):
    print(
        f"Sala {sala + 1} - {vagos} lugar(es) vazio(s) - {vendidos[sala]} lugares vendidos"
    )
print("total de lugares vendidos: " + str(sum(lugares for lugares in vendidos)))
