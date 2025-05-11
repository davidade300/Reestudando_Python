# exemplo de tratamento de exceção simples

nomes: list = ["Ana", "Carlos", "Magno"]

for tentativa in range(3):
    try:
        i = int(input("Digite o indice que quer imprimir:"))
        print(nomes[i])
    except Exception as e:
        print(f"Algo de errado aconteceu: {e}")

### com finally ###
for tentativa in range(3):
    try:
        i = int(input("Digite o indice que quer imprimir: (com finally)"))
        print(nomes[i])
    except ValueError as e:
        print(f"Algo de errado aconteceu: {e}")
    finally:  # o bloco finally é executado não importa se erro ou não
        print(f"tentativa {tentativa + 1}")


### Utilizando raise ###

for tentativa in range(3):
    try:
        i = int(input("Digite o indice que quer imprimir: (com raise)"))
        print(nomes[i])
    except ValueError:
        print("Digite um numero")
        raise  # propaga a exceção até o proximo bloco try ou encerra o programa
        # chamando o stackstrace caso não exista bloco try
    finally:
        print("Sempre o finally é executado")
