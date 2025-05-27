# Programa 9.6: Controle de uma agenda de telefone

agenda = []


def pede_nome():
    return input("Nome: ")


def pede_telefone():
    return input("Telefone:")


def mostra_dados(nome, telefone):
    print(f"Nome: {nome} Telefone: {telefone}")


def pede_nome_arquivo():
    return input("Nome do arquivo: ")


def pesquisa(nome):
    mnome = nome.lower()
    for p, e in enumerate(agenda):
        if e[0].lower() == mnome:
            return p

    return None


def novo():
    nome = pede_nome()
    telefone = pede_telefone()

    agenda.append([nome, telefone])


def apaga():
    nome = pede_nome()
    p = pesquisa(nome)

    if p is not None:
        del agenda[p]

    else:
        print("Nome não encontrado.")


def altera():
    p = pesquisa(pede_nome())

    if p is not None:
        nome = agenda[p][0]
        telefone = agenda[p][1]

        print("Encontrado:")
        mostra_dados(nome, telefone)
        nome = pede_nome()
        telefone = pede_telefone()

        agenda[p] = [nome, telefone]
    else:
        print("Nome não encontrado.")


def lista():
    print("\nAgenda\n\n------")

    for e in agenda:
        mostra_dados(e[0], e[1])
        print(f"posicao: {agenda.index(e) + 1}")
        print("------\n")


def le():
    global agenda

    nome_arquivo = pede_nome_arquivo()

    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        agenda = []

        for linha in arquivo.readlines():
            nome, telefone = linha.strip().split(sep="#")


def grava():
    nome_arquivo = pede_nome_arquivo()
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        for e in agenda:
            arquivo.write(f"{e[0]}#{e[1]}\n")


def ordena_por_nome():
    global agenda
    # for pessoa in agenda:
    # agenda.sort(key=pessoa[0])
    # return sorted(agenda,key=pessoa[0])


def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return valor
        except ValueError:
            print(f"Valor invalido, favor digitar entre {inicio} e {fim}")


def menu():
    print("""
1 - Novo
2 - Altera
3 - Apaga
4 - Lista
5 - Grava
6 - Lê
          

0 - sai
""")

    return valida_faixa_inteiro("Escolha uma opcao: ", 0, 7)


while opcao := menu():
    print(f"{len(agenda)}")

    if opcao == 0:
        break

    elif opcao == 1:
        novo()

    elif opcao == 2:
        altera()

    elif opcao == 3:
        apaga()

    elif opcao == 4:
        lista()

    elif opcao == 5:
        grava()

    elif opcao == 6:
        le()

    elif opcao == 7:
        ordena_por_nome()
