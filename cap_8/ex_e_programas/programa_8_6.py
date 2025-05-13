# Fatorial escrito de forma recursiva com logs


def fatorial(numero: int):
    print(f"calculando o fatorial de {numero}")
    if (numero == 0) or (numero == 1):
        print(f"fatorial de {numero} = 1")
        return 1
    else:
        fat = numero * fatorial(numero - 1)
        print(f"fatorial de {numero} = {fat}")
        return fat


print(fatorial(5))
