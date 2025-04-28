# Programa que lê 3 strings, imprime o resultado da substituição na primeira,
# dos caracteres da segunda pelos da terceira

texto_1: str = "AATTCGAA"
texto_2: str = "TG"
texto_3: str = "AC"

if len(texto_2) == len(texto_3):
    resultado: str = ""

    for letra in texto_1:
        posicao: int = texto_2.find(letra)
        if posicao != -1:
            resultado += texto_3[posicao]
        else:
            resultado += letra

    if resultado == "":
        print("todos os caracteres foram removidos")
    else:
        print(
            f"Os caracteres {texto_2} foram substituidos por {texto_3} em {texto_1} gerando: {resultado}"
        )
else:
    print("As strings devem ter o mesmo tamanho")
