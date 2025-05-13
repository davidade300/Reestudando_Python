# Programa 8.23: Jogo do alienigena:

import random

MAX_TENTATIVAS = 3

arvore = random.randint(1, 100)

print("Um alienigena está escondido atrás de uma árvore")
print("Cada árvore foi numerada de 1 a 100.")
print("Você tem 3 tentativas para advinhar em que árvore")
print("o alienigena se esconde")
print(arvore)

for tentativa in range(MAX_TENTATIVAS + 1):
    palpite = int(input(f"Arvore {tentativa}/ {MAX_TENTATIVAS}: "))

    if palpite == arvore:
        print(f"Você acertou na {tentativa}\u00aa tentativa")
        break
    elif palpite > arvore:
        print("Muito alto")
    else:
        print("Muito baixo")
else:
    print("Você não conseguiu acertar.")
    print(f"O alienigena estava na árvore {arvore}")
