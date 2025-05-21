# Função que gera números semelhate a função range.
# A função recebe 3 paramêtros e o comportamento deve mudar de acordo com a quantidade
# de paramêtros passados.
# Ex.: list(faixa(1)) >>> [0,1]
# list(faixa(1,10)) >>> [1,2,3,4,5,6,7,8,9,10]
# list(faixa(0,10,2)) >> [0,2,4,6,8,10]


def faixa(inicial, fim=None, passo=1):
    if fim is None:
        inicial, fim = 0, inicial

    atual = inicial

    while atual <= fim:
        yield atual
        atual += passo


list(faixa(1, 10))
