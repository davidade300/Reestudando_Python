# Programa 6.8: Pilha de pratos (stack)

prato = 5
pilha: list = list(range(1, prato + 1))

while True:
    print(
        f"\nExistem {len(pilha)} pratos na pilha\
          \n Pilha atual: {pilha}\
          \n Digite E para empillhar um novo prato,\
          \n ou D para desempilhar. S para sair."
    )

    operacao = input("Operação (E, D ou S): ")

    if operacao == "D":
        if len(pilha) > 0:
            lavado = pilha.pop(
                -1
            )  # como um stack é LIFO começamos a remover pelo último índice
            print(f"Prato {lavado} lavado")
        else:
            print("Pilha vazia! nada para lavar.")

    elif operacao == "E":
        prato += 1  # novo prato
        pilha.append(prato)

    elif operacao == "S":
        break

    else:
        print("\nOperação inválda! Digite apenas E, D ou S!")
