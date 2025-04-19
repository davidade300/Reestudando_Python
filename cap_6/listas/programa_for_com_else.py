# É possível usar else com "for" e com "while"
lista: list = [7, 9, 10, 12]

p = int(input("digite o número a pesquisar: "))

for item in lista:
    if p == item:
        print("elemento encontrado")
        break

else:
    print("Elemento não encontrado")
