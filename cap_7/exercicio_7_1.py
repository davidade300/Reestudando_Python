# Programa que lê duas strings, verifica se a segunda ocorre dentro da primeira
# e imprime a posição de inicio

texto_1: str = "AABBEFAATT"
texto_2: str = "BE"

print(f"{texto_2} encontrado na posição {texto_1.find(texto_2)} de {texto_1}")
