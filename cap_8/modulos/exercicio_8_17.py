# Programa 8.23 modificado para ter níveis de dificuldade

import random

DIFICULDADE: dict = {
    "facil": [5, 20, 100],
    "medio": [10, 25, 80],
    "dificil": [20, 30, 70],
}
try:
    configuracao = input(
        "Escolha a sua dificuldade: facil, medio, dificil: "
    ).lower()
    MAX_VIDA = DIFICULDADE[configuracao][2]
    DANO_MAXIMO = DIFICULDADE[configuracao][1]
    DANO_MINIMO = DIFICULDADE[configuracao][0]
except Exception:
    raise KeyError("as opcoes sao: facil, medio ou dificil") from None


vida = MAX_VIDA
arvore = random.randint(1, 100)

print("Um alienigena está escondido atrás de uma árvore")
print("Cada árvore foi numerada de 1 a 100.")
print(f"Você tem {vida} tentativas para advinhar em que árvore")
print("o alienigena se esconde")
# print(arvore)


while vida > 0:
    palpite = int(input(f"vida {vida}/{MAX_VIDA}: "))

    if palpite == arvore:
        print(f"Você acertou com {vida}/{MAX_VIDA} de vida")
        break
    elif palpite > arvore:
        print("Muito alto")
        vida -= random.randint(DANO_MINIMO, DANO_MAXIMO)
    else:
        print("Muito baixo")
        vida -= random.randint(DANO_MINIMO, DANO_MAXIMO)

else:
    print("Você perdeu toda a sua vida")
    print(f"O alienigena estava na árvore {arvore}")
