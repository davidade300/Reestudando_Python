# O bloco try também pode se rusado com else, assim como while e for.
# o bloco else é executado somente se não ouver exceção no bloco try e pode ser
# combinado com except e finally

while True:
    try:
        v = int(input("Diite um número inteiro (0 sai): "))

        if v == 0:
            break
    except Exception:
        print("Valor inválido! Redigite")
    else:
        print("Parabéns, nenhuma exceção")
    finally:
        print("Executando sempre, mesmo com break")
