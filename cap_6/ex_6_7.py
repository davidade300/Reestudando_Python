# Programa para leitura de expressão com parênteses usando stacks e
# verifica se os parênteses foram abertos e fechados na ordem correta

stack: list = []
while True:
    entrada: str = input('Digite "(", ")", (0 para sair): ')

    if entrada == "0":
        break

    stack.append(entrada)
