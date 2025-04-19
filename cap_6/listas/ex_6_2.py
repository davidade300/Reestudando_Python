l1: list = []
l2: list = []
result_l: list = []

contador: int = 0
entrada: int = 0
while True:
    entrada = int(
        input(f"digite o {contador + 1}º valor da lista 1 (0 para sair):")
    )

    if entrada == 0:
        break

    l1.append(entrada)

    entrada = int(
        input(f"digite o {contador + 1}º valor da lista 2 (0 para sair):")
    )
    l2.append(entrada)

    contador += 1

# result_l.extend(l1)
result_l = l1[:]  # cria uma cópia(novo objeto em memória em vez de nova ref
# ao msm objetos) com todos os elementos da lista

result_l.extend(l2)

print(result_l)
