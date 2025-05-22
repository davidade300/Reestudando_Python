arquivo = open("numeros.txt", "w")
for linha in range(1, 100):
    arquivo.write(f"{linha}\n")
arquivo.close()
