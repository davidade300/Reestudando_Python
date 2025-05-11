# Programa 8.16: Funcao imprime_maior com numero indeterminado de parametros


def imprime_maior(mensagem, *numeros):
    maior = None
    for e in numeros:
        if maior is None or maior < e:
            maior = e
    print(mensagem, maior)


imprime_maior("Maior", 5, 4, 3, 1)
imprime_maior("Max:")
