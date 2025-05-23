# Programa que inverte a order das linhas do arquivo pares.txt


pares = open("pares.txt", "r")
serap = open("serap.txt", "w")


serap.writelines(pares.readlines()[-1::-1])

pares.close()
serap.close()
