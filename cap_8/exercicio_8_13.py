# função que recebe uma string com opções validas a aceitar (cada opção é uma letra )
# e converte as opções validas para minusculas

opt: str = input("Digite as opções validas(sem espaços): ").lower()


def valida_opts(validas):
    while True:
        entrada = input("Digite a opcao selecionada: ").lower()

        if entrada in list(validas):
            break
        print("Erro: opção inválida. Redigite.\n")

    return entrada


print(valida_opts(validas=opt))
