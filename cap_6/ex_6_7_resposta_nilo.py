# Resposta do livro ao ex 6.7
# A resposta do livro gera resposta "OK" para lista vazia
expressao = input("Digite a sequência de parênteses a vaidar: ")

x = 0
pilha = []

while x < len(expressao):
    if expressao[x] == "(":
        pilha.append("(")

    if expressao[x] == ")":
        if len(pilha) > 0:
            topo = pilha.pop(-1)
        else:
            pilha.append(")")  # Força a mensagem de erro
            break

    x += 1

if len(pilha) == 0:
    print(pilha)
    print("OK")
else:
    print(pilha)
    print("Erro")
