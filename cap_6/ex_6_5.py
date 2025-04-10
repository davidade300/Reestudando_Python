# Simulação de fila de banco

ultimo = 10
fila = list(range(1, ultimo + 1))

lista_operacoes: list = []
while True:
    print(
        f"\nExistem {len(fila)} cliente nas fila\
          \nFila atual: {fila}\
          \nDigite F para adicionar um cliente ao fim da fila, \
          \nou A para realizar o atedimento. S para sair."
    )

    operacao = input("Operacao (F, A ou S), 0 para sair: ")

    if operacao == "S":
        break

    lista_operacoes.append(operacao)
    print(lista_operacoes)

x = 0
while x < len(lista_operacoes):
    if lista_operacoes[x] == "A":
        if len(fila) > 0:
            atendido = fila.pop(0)
            print(f"Cliente {atendido} atendido")
        else:
            print("Fila vazia! ninguem para atender")

    elif lista_operacoes[x] == "F":
        ultimo += 1  # Incremente o ticket do novo cliente
        fila.append(ultimo)
        print(fila)

    elif lista_operacoes[x] == "S":
        break
    else:
        print('operação invalida! Digite apenas "F", "A" ou "S"!\n')
        break

    x += 1
