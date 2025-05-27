entrada = open("entrada.txt", "r", encoding="utf-8")
saida = open("saida_2.txt", "w", encoding="utf-8")
ocorrencias: dict = {}
contador = 0

for linha in entrada.readlines():
    for palavra in linha:
        if palavra.strip() not in ocorrencias.keys():
            ocorrencias[palavra.strip()] = 0

        if palavra.strip() in ocorrencias.keys():
            ocorrencias[palavra.strip()] += 1

print(ocorrencias)

for k, v in ocorrencias.items():
    saida.write(f"{k}: {v} \n")

entrada.close()
saida.close()
