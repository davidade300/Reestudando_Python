# Exercicio 10.11:


class Cidade:
    def __init__(self, nome: str, populacao: int) -> None:
        self.nome = nome
        self.populacao = populacao
        self.estado: Estado | None = None

    def __str__(self) -> str:
        return f"Cidade (nome={self.nome}, população={self.populacao}, estado={self.estado})"


class Estado:
    def __init__(self, nome: str, sigla: str, cidades: list = []) -> None:
        self.nome = nome
        self.sigla = sigla
        self.cidades: list[Cidade] = cidades

    def adiciona_cidade(self, cidade: Cidade):
        cidade.estado = self
        self.cidades.append(cidade)

    def populacao(self) -> int:
        return sum([c.populacao for c in self.cidades])


am = Estado("Amazonas", "AM")
am.adiciona_cidade(Cidade("Manaus", 1861838))
am.adiciona_cidade(Cidade("Parintins", 103828))
am.adiciona_cidade(Cidade("Itacoatiara", 89064))

sp = Estado("São Paulo", "SP")
sp.adiciona_cidade(Cidade("São Paulo", 11376685))
sp.adiciona_cidade(Cidade("Guarulhos", 1244518))
sp.adiciona_cidade(Cidade("Campinas", 1098630))

rj = Estado("Rio de Janeiro", "RJ")
rj.adiciona_cidade(Cidade("Rio de Janeiro", 6390290))
rj.adiciona_cidade(Cidade("São Gonçalo", 1016128))
rj.adiciona_cidade(Cidade("Duque de Caixias", 867067))


for estado in [am, sp, rj]:
    print(f"Estado: {estado.nome} Sigla: {estado.sigla}")
    for cidade in estado.cidades:
        print(f"Cidade: {cidade.nome} População: {cidade.populacao}")
    print(f"População do Estado: {estado.populacao()}\n")
