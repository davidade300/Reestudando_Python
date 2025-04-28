# Programa que lê duas strings e gera uma terceira com os caracteres comums as
# duas strings lidas

texto_1: str = "AAACTBF"
texto_2: str = "CBT"
texto_3: str = ""
# comums: list = [char for char in texto_1 if char in texto_1 and char in texto_2]
#
# texto_3: str = "".join(comums)
# print(texto_3)

for letra in texto_1:
    if letra in texto_1 and letra in texto_2:
        texto_3 += letra

if texto_3 == "":
    print("caracteres comums não encontrados")
else:
    print(f"caracteres comums: {texto_3}")
