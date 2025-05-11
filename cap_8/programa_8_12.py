# Função retangulo com parâmetros obrigatórios e opcionais


def retangulo(largura, altura, char="*"):
    linha = char * largura

    for i in range(altura):
        print(linha)


retangulo(3, 4)
