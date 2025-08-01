import json

agenda = []


def pede_nome():
    return input("Nome: ")


def pede_telefone():
    return input("Telefone: ")


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
    print("------\n")


def lê():
    global agenda
    nome_arquivo = pede_nome_arquivo()
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            agenda = json.load(arquivo)
    except FileNotFoundError:
        print("Arquivo não encontrado")
    except json.JSONDecodeError:
        print("Erro ao ler o arquivo JSON")


def grava():
    nome_arquivo = pede_nome_arquivo()
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(agenda, arquivo, ensure_ascii=False, indent=2)


def valida_faixa_inteiro(pergunta, início, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if início <= valor <= fim:
                return valor
        except ValueError:
            print(f"Valor inválido, favor digitar entre {início} e {fim}")


def menu():
    print(
        """
  1 – Novo
  2 – Altera
  3 – Apaga
  4 – Lista
  5 – Grava
  6 – Lê

  0 – Sai
"""
    )
    return valida_faixa_inteiro("Escolha uma opção: ", 0, 6)


while opção := menu():
    if opção == 0:
        break
    elif opção == 1:
        novo()
    elif opção == 2:
        altera()
    elif opção == 3:
        apaga()
    elif opção == 4:
        lista()
    elif opção == 5:
        grava()
    elif opção == 6:
        lê()
