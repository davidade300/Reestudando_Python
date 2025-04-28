# Programa que lê duas strings e gera uma terceira apenas com os caracteres que
# aparecem e uma delas

texto_1: str = "CTA"
texto_2: str = "ABC"

texto_3: set = set(texto_1) ^ set(texto_2)
resultado: str = "".join(texto_3)

print(f"string resultante: {resultado}")
