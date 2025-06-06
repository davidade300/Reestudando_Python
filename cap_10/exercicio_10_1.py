# Exercicio 10.1


class Televisao:
    def __init__(self) -> None:
        self.ligada: bool = False
        self.canal: int = 2
        self.tamanho = 0
        self.marca = "toshiba"


tv_1 = Televisao()
tv_1.tamanho = 2
tv_1.marca = "ll"

print(tv_1.marca, tv_1.tamanho)

tv_2 = Televisao()
tv_2.tamanho = 4
tv_2.marca = "asdf"

print(tv_2.marca, tv_2.tamanho)
