# Programa 8.22 alterado para fornecer 3 chances ao usuário
import random

n = random.randint(1, 10)
x = int(input("Escolha um número entre 1 e 10: "))

for i in range(2):
    print(f"Tentativa {i + 1}")
    x = int(input("Escolha um número entre 1 e 10: "))

    if x == n:
        print("Voce acerto!")
    else:
        print("você errou")
        i += 1
else:
    print("fim de jogo!")
