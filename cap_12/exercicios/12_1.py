# Programa 12.1 modificado para reconhecer sequencias de letras
entrada: str = "ABC431DEF901c431203FXEW9"
saida: list = []
numero: list = []

for caractere in entrada:
    if "a" <= caractere.lower() <= "z":
        if not numero:
            saida.append(numero)

        numero += caractere

    elif numero:
        numero: list = []

for encontrado in saida:
    print("".join(encontrado))
