# Programa 8.22: Advinhando o número
import random

n = random.randint(1, 10)
x = int(input("Escolha um número entre 1 e 10: "))

if x == n:
    print("Voce acerto!")
else:
    print("você errou")
