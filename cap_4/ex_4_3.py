a: float = float(input("digite o 1 numero: "))
b: float = float(input("digite o 2 numero: "))
c: float = float(input("digite o 3 numero: "))

maior = a

if b > a and b > c:
    maior = b

if c > a and c > b:
    maior = c

menor = a

if b < c and b < a:
    menor = b

if c <= a and c < b:
    menor = c

print(
    f" o maior numero digitado foi {maior}\n o menor numero digitado foi: {menor}"
)
