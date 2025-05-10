# função que compara uma lista e uma string, se string em lista
# retorna verdadeiro, se não, falso


def cmp_str_list(texto, lista):
    palavra = ""

    for elemento in list(texto):
        if elemento in lista:
            palavra += elemento

    return palavra == texto


print(cmp_str_list("asdr", ["a", "s", "d", "f", "g"]))
print(cmp_str_list("asdf", ["a", "s", "d", "f", "g"]))


### solução do autor ###
def procura_string(s, lista):
    return s in lista
