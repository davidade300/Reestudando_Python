dividendo = int(input("digite o dividendo: "))
divisor = int(input("digite o divisor: "))

quociente = 0  # resultado
x = dividendo  # ńumero a ser divido

while x >= divisor:
    x = x - divisor
    quociente += 1

print(quociente)
