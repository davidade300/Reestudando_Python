# Programa para leitura de expressão com parênteses usando stacks e
# verifica se os parênteses foram abertos e fechados na ordem correta

stack: list = []
palavra: list = []


while True:
    entrada: str = input('Digite "(", ")", (0 para sair): ')

    if entrada == "0":
        break

    stack.append(entrada)

if len(stack) % 2 == 0:
    while len(stack) != 0:
        if stack[0] == "(":
            palavra += stack[0]
            stack.pop(0)

        if stack[-1] == ")":
            palavra += stack[-1]
            stack.pop(-1)

if len(palavra) != 0:
    print(f"{palavra}  OK")
else:
    print(f"{stack}   ERRO")
