# Programa que lê duas strings e gera uma terceira, com os caracteres da
# segunda que foram retirados da primeira

texto_1: str = "AATTGGAA"
texto_2: str = "TG"

resultado: str = ""

for char in texto_1:
    if char not in texto_2:
        resultado += char

print(resultado)
