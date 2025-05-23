arquivo = open("numeros.txt", "w")
for linha in range(1, 100):
    arquivo.write(f"{linha}\n")
arquivo.close()

#######

with open("multiplos_de_4", "w") as multiplos_4:
    with open("pares.txt") as pares:
        for linha in pares.readlines():
            if int(linha) % 4 == 0:
                multiplos_4.write(linha)
