# reescrita da função map:

"""A função map (a built-in) recebe uma função e um iterável | lista
e aplica a função a cada item desse iteravel | lista
"""


def map_1(funcao, valores):
    retorno = []

    for v in valores:
        retorno.append(funcao(v))
    return retorno


### Usando zip para deixar mais proximo com o map built-in


def map_2(funcao, *valores):
    retorno = []

    for v in zip(*valores):
        retorno.append(funcao(*v))
    return retorno


map_2(lambda a, b: (a, b), [1, 2, 3], [4, 5, 6])

### retornando um gerador, como a função map do python


def map_3(funcao, *valores):
    for v in zip(*valores):
        yield funcao


map_3(lambda a, b: (a, b), [1, 2, 3], [4, 5, 6])

list(map_3(lambda a, b: (a, b), [1, 2, 3], [4, 5, 6]))
