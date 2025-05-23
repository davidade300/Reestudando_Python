# programa que lê os arquivos pares.txt e impares.txt e criar um só arquivo com
# todas as linhas dos dois arquivos, preservando a ordem numérica


def read_number(file):
    while True:
        n = file.readline()

        if n == "":
            return None
        if n.strip() != "":
            return int(n)


def write_number(file, number):
    file.write(f"{number}\n")


pares = open("pares.txt", "r")
impares = open("impares.txt", "r")
pares_impares = open("paresimpares.txt", "w")

n_par = read_number(pares)
n_impar = read_number(impares)

while True:
    if n_par is None and n_impar is None:
        break

    if n_par is not None and (n_impar is None or n_par <= n_impar):
        write_number(pares_impares, n_par)
        n_par = read_number(pares)

    if n_impar is not None and (n_par is None or n_impar <= n_par):
        write_number(pares_impares, n_impar)
        n_impar = read_number(impares)

pares_impares.close()
pares.close()
impares.close()
