# Exercicio 8.16: Jogo do alienigena modificado para representar a vida do jogador

import random

MAX_VIDA = 100
MAX_TENTATIVAS = 3
vida = MAX_VIDA

arvore = random.randint(1, 100)

print("Um alienigena está escondido atrás de uma árvore")
print("Cada árvore foi numerada de 1 a 100.")
print("Você tem 3 tentativas para advinhar em que árvore")
print("o alienigena se esconde")
# print(arvore)


while vida > 0:
    palpite = int(input(f"vida {vida}/{MAX_VIDA}: "))

    if palpite == arvore:
        print(f"Você acertou com {vida}/{MAX_VIDA} de vida")
        break
    elif palpite > arvore:
        print("Muito alto")
        vida -= random.randint(5, 20)
    else:
        print("Muito baixo")
        vida -= random.randint(5, 20)

else:
    print("Você perdeu toda a sua vida")
    print(f"O alienigena estava na árvore {arvore}")
