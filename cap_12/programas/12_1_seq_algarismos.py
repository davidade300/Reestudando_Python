entrada: str = "ABC431DEF901c431203FXEW9"
saida: list = []
numero: list = []

for caractere in entrada:
    if "0" <= caractere <= "9":
        if not numero:
            saida.append(numero)

        numero += caractere

    elif numero:
        numero: list = []

for encontrado in saida:
    print("".join(encontrado))
