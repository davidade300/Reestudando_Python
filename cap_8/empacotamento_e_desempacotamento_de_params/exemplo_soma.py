# Exemplo com a funcao soma
def soma(a, b):
    print(a + b)


L = [2, 3]

soma(*L)
print()

# Exemplo com uma lista de listas e varias chamadas de funcao em um for loop


def barra(n=10, c="*"):
    print(c * n)


L = [[5, "-"], [10, "*"], [6, "."]]

for e in L:
    barra(*e)
