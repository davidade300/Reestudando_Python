"""Reconhecendo numero de telefone"""

entrada = "Compre por R$50,72. Ligue já (92)5431-2201 antes de 10/12/2033."
Saída = []
telefone = []


def numero(entrada: str, qmim: int, qmax: int):
    num: int = 0
    for caractere in entrada:
        if caractere.isnumeric():
            num += 1

        else:
            break

    if qmim <= num <= qmax:
        return True, 0, num - 1

    return False


def ddd(entrada: str):
    estado = posicao = 0
    codigo_ddd: list = []

    while posicao < len(entrada):
        caractere = entrada[posicao]

        if estado == 0 and caractere == "(":
            estado = 1
            codigo_ddd.append(caractere)

        elif estado == 1:
            achou, inicio, fim = numero(entrada[posicao:], 2, 3)  # type: ignore

            if achou:
                codigo_ddd.append(entrada[posicao + inicio : posicao + fim + 1])
                estado = 2
                posicao += fim

            else:
                break

        elif estado == 2:
            if caractere == ")":
                return True, 0, posicao

            break

        else:
            break

        posicao += 1

    return False, -1, -1


for posicao in range(len(entrada)):
    achou, inicio, fim = ddd(entrada[posicao:])

    if achou:
        print(f"DDD encontrado nas posicoes: {inicio + fim} a {posicao + fim}")
        print(entrada[posicao + inicio : posicao + fim + 1])
