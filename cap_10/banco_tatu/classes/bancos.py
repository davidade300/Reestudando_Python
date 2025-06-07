from contas import Conta


class Banco:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.contas: list[Conta] = []

    def abre_conta(self, conta: Conta):
        self.contas.append(conta)

    def lista_contas(self):
        for c in self.contas:
            c.resumo()
