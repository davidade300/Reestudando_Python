multiplicado = int(input("digite o valor do multipicado"))
multiplicando = int(input("digite o valor do multiplicando"))

contador = 1
resultado = 0

while contador <= multiplicando:
    resultado += multiplicado
    contador += 1

print(resultado)
