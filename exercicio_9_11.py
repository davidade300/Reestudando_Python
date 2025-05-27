entrada = open("entrada.txt", "r", encoding="utf-8")

ocorrencias: dict = {}
contador = 0

for linha in entrada.readlines():
    for palavra in linha:
        if palavra.strip() not in ocorrencias.keys():
            ocorrencias[palavra.strip()] = 0

        if palavra.strip() in ocorrencias.keys():
            ocorrencias[palavra.strip()] += 1

print(ocorrencias)

entrada.close()
