# Jogo da forca modificado para usar uma lista de palavras e
# calcular um índice a ser utilizado

lista_de_palavras: list = []
qtd_palavras: int = int(
    input("Digite a quantidade de palavras a serem adicionados na lista: ")
)

for i in range(qtd_palavras):
    palavra = input(f"Digite a {i + 1}º palavra secreta: ").lower().strip()
    lista_de_palavras.append(palavra)

    i += 1

indice: int = (int(input("digite um número: ")) * 776) % len(lista_de_palavras)

escolhida: str = lista_de_palavras[indice]

print(escolhida)

for x in range(100):
    print()

digitadas: list = []
acertos: list = []
erros: int = 0

while True:
    senha = ""

    for letra in escolhida:
        senha += letra if letra in acertos else "."
    print(senha)

    if senha == escolhida:
        print("você acertou!")
        break

    tentativa = input("\nDigite uma letra: ").lower().strip()

    if tentativa in digitadas:
        print("você já tentou esta letra!")
        continue
    else:
        digitadas += tentativa

        if tentativa in escolhida:
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
        print(escolhida)
        break
