# Exercicio 9.34:Programa 7.2 modificado para imprimir a duração das partidas

import time

palavra = input("Digite a palavra secreta: ").lower().strip()

hora_inicio = time.time()

for x in range(100):
    print()

digitadas: list = []
acertos: list = []
erros: int = 0

while True:
    senha = ""

    for letra in palavra:
        senha += letra if letra in acertos else "."
    print(senha)

    if senha == palavra:
        print("você acertou!")
        print(f"tempo de partida: {(time.time() - hora_inicio):.2f} segundos")
        break

    tentativa = input("\nDigite uma letra: ").lower().strip()

    if tentativa in digitadas:
        print("você já tentou esta letra!")
        continue
    else:
        digitadas += tentativa

        if tentativa in palavra:
            acertos += tentativa

        else:
            erros += 1
            print("você errou!")

    print("x==:==\nX  :  ")
    print("X  O  " if erros >= 1 else "X")

    linha2: str = ""

    if erros == 2:
        linha2 = "  |  "
    elif erros == 3:
        linha2 = " \| "  # type: ignore
    elif erros >= 4:
        linha2 = " \|/ "  # type: ignore

    print(f"X{linha2}")
    linha3: str = ""

    if erros == 5:
        linha3 += " /  "
    elif erros >= 6:
        linha3 += " / \ "  # type: ignore

    print(f"X{linha3}")
    print("X\n===========")

    if erros == 6:
        print("Enforcado!")
        print(f"tempo de partida: {(time.time() - hora_inicio):.2f} segundos")
        break
