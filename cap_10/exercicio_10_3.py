# Exercicio 10.3:


class Televisao:
    def __init__(self, canal_inicial: int, min: int = 2, max: int = 14) -> None:
        self.ligada: bool = False
        self.canal = canal_inicial
        self.cmin = min
        self.cmax = max

    def muda_canal_para_baixo(self):
        if self.canal - 1 >= self.cmin:
            self.canal -= 1

        if self.canal < self.cmin:
            self.canal = self.cmax

            return self.canal

    def muda_canal_para_cima(self):
        if self.canal + 1 <= self.cmax:
            self.canal += 1

        if self.canal > self.cmax:
            self.canal = self.cmin

            return self.canal


tv = Televisao(5, 1, 99)

print(tv.muda_canal_para_baixo())

tv_2 = Televisao(canal_inicial=0, min=4, max=10)
tv_3 = Televisao(canal_inicial=0, min=5, max=11)
