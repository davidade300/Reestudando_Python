# Simulação de fila de banco
ultimo = 10
fila = list(range(1, ultimo + 1))

while True:
    print(
        f"\nExistem {len(fila)} cliente nas fila\
          \nFila atual: {fila}\
          \nDigite F para adicionar um cliente ao fim da fila, \
          \nou A para realizar o atedimento. S para sair."
    )

    operacao = input("Operacao (F, A ou S): ")

    if operacao == "A":
        if len(fila) > 0:
            atendido = fila.pop(0)
            print(f"Cliente {atendido} atendido")
        else:
            print("Fila vazia! ninguem para atender")

    elif operacao == "F":
        ultimo += 1  # Incrementa o ticket do novo cliente
        fila.append(ultimo)

    elif operacao == "S":
        break
    else:
        print('operação invalida! Digite apenas "F", "A" ou "S"!\n')
