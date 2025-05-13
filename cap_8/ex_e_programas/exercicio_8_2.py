# função que recebe 2 numeros e retorna true se o 1º for multiplo do 2º


def multiplo(a, b):
    if b == a:
        return True

    if a % b != 0:
        return False

    return True


print(multiplo(8, 4))
print(multiplo(7, 3))
print(multiplo(5, 5))
