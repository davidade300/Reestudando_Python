from clientes import Cliente


class Conta:
    def __init__(
        self, clientes: list[Cliente], numero: str, saldo: float = 0
    ) -> None:
        self.clientes = clientes
        self.numero = numero
        self.saldo = 0
        self.operacoes: list = []
        self.deposito(saldo)

    def resumo(self):
        print(f"CC numero: {self.numero} Saldo: {self.saldo:10.2f}")

        for cliente in self.clientes:
            print(f"Nome: {cliente.nome}\nTelefone: {cliente.telefone}\n")

    def saque(self, valor: float):
        if self.pode_sacar(valor):
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor])

            return True

        if valor > self.saldo:
            print("saldo insuficiente")

            return False

    def pode_sacar(self, valor: float):
        return self.saldo >= valor

    def deposito(self, valor: float):
        self.saldo += valor
        self.operacoes.append(["DEPOSITO", valor])

    def extrato(self):
        print(f"EXTRATO CC Nº {self.numero}\n")

        for operacao in self.operacoes:
            print(f"{operacao[0]:10s} {operacao[1]:10.2f}")

        print(f"\n Saldo: {self.saldo:10.2f}\n")


class ContaEspecial(Conta):
    def __init__(
        self,
        clientes: list[Cliente],
        numero: str,
        saldo: float = 0,
        limite: float = 0,
    ) -> None:
        super().__init__(clientes, numero, saldo)
        self.limite = limite

    def saque(self, valor: float):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor])

            return True

        if valor >= self.saldo + self.limite:
            print("saldo insuficiente")

            return False

    def pode_sacar(self, valor):
        return self.saldo + self.limite >= valor

    def extrato(self):
        print(f"EXTRATO CC Nº {self.numero}\n")

        for operacao in self.operacoes:
            print(f"{operacao[0]:10s} {operacao[1]:10.2f}")

        print(f"\n Limite total para saque: {(self.saldo + self.limite):10.2f}")
        print(f"\n Saldo: {self.saldo:10.2f}\n")
