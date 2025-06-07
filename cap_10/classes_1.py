# Arquivo com classes para os programas do cap 10


class Televisao:
    def __init__(self, canal_inicial: int, min: int = 2, max: int = 14) -> None:
        self.ligada: bool = False
        self.canal = canal_inicial
        self.cmin = min
        self.cmax = max

    def muda_canal_para_baixo(self):
        if not self.ligada:
            return

        if self.canal - 1 >= self.cmin:
            self.canal -= 1

        if self.canal < self.cmin:
            self.canal = self.cmax

        return self.canal

    def muda_canal_para_cima(self):
        if not self.ligada:
            return

        if self.canal + 1 <= self.cmax:
            self.canal += 1

        if self.canal > self.cmax:
            self.canal = self.cmin

        return self.canal


class Pilha:
    def __init__(self, energia: int = 100) -> None:
        self.energia = energia

    def consuma(self, consumo):
        if consumo > self.energia:
            consumo = self.energia  # consome toda a energia

        self.energia -= consumo

        return consumo


class ControleRemoto:
    def __init__(self, televisao: Televisao, pilha: Pilha) -> None:
        self.televisao = televisao
        self.pilha = pilha

    def liga(self):
        if self.pilha.consuma(1):
            self.televisao.ligada = True

    def desliga(self):
        if self.pilha.consuma(1):
            self.televisao.ligada = False

    def canal_mais(self):
        if self.pilha.consuma(1):
            self.televisao.muda_canal_para_cima()

    def canal_menos(self):
        if self.pilha.consuma(1):
            self.televisao.muda_canal_para_baixo()
