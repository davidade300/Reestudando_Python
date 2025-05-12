# O bloco finally é executado independente de termos uma exceção ou não
# pode ser lido como:
# "Execute esse bloco, mesmo que aconteça uma excecao com ou sem tratamento"
# o bloco finally, dentro de uma função, é executado antes de a função retornar, mesmo que ocorra exceção


def par(n):
    try:
        return n % 2
    finally:
        print("Executado antes de retornar")


try:
    print(2, par(2))
    print("A", par("A"))

except Exception:
    print("Algo de errado aconteceu")

# também é possível criar nossas propias exceções utilizando raise


def par_2(n):
    try:
        return n % 2
    except Exception:
        raise ValueError("Valor invalido")
