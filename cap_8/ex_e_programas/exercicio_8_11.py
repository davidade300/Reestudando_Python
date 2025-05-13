# função que valida string


def valida_string(entrada, min, max):
    if type(entrada) is not str:
        print(f"{entrada} não é uma string")

        return False

    if len(entrada) < min or len(entrada) > max:
        print(f"{entrada} não está dentro dos parametros aceitos!")

        return False

    return True


print(valida_string("asdf", 1, 4))
