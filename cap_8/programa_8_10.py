# Validação de inteiro usando função


def faixa_int(pergunta, min, max):
    while True:
        v = int(input(pergunta))

        if v < min or v > max:
            print(f"Valor inválido. Digite um valor entre {min} e {max}")

        else:
            return v
