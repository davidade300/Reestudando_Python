# Programa 8.26 modificado para receber 2 params opcionais,
# 1 para indicar o caracter a ser imprimido antes do numero, sendo " " o padrão,
# o segundo é quantos caracteres adicionar por nível, 2 sendo o padrão


def imprime_lista(lista, nivel=0, caracter=" ", chars_nivel=2):
    for x in lista:
        if isinstance(x, int):
            print(
                f"{nivel * 2 * caracter}{x}"
            )  # por padrão o padding é a esquerda
        else:
            imprime_lista(x, nivel + 1, caracter, chars_nivel)


imprime_lista([1, [2, 3, 4], [5, 6, [7, 8, 9]], 10], caracter="*")
