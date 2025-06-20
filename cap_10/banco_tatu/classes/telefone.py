"""https://python.nilo.pro.br/extras/4/capitulo10/agenda_completa/"""

from functools import total_ordering

from banco_tatu.lista_unica import ListaUnica

from .nome import Nome


@total_ordering
class Tipotelefone:
    def __init__(self, tipo) -> None:
        self.tipo = tipo

    def __str__(self) -> str:
        return f"({self.tipo})"

    def __eq__(self, other) -> bool:
        if other is None:
            return False

        return self.tipo == other.tipo

    def __lt__(self, other):
        return self.tipo < other.tipo


class Telefone:
    def __init__(self, numero: str, tipo: Tipotelefone | None = None) -> None:
        self.numero: str = numero
        self.tipo = tipo

    def __str__(self) -> str:
        tipo = self.tipo or ""

        return f"{self.numero} {tipo}"

    def __eq__(self, other) -> bool:
        return self.numero == other.numero and (
            (self.tipo == other.tipo)
            or (self.tipo is None or other.tipo is None)
        )

    @property
    def numero(self) -> str:  # type: ignore
        return self.__numero  # type: ignore

    @numero.setter
    def numero(self, valor: str) -> None:  # type: ignore
        if valor is None or not valor.strip():
            raise ValueError("Numero nao pode ser None ou em branco")
        self.__numero = valor


class Telefones(ListaUnica):
    def __init__(self) -> None:
        super().__init__(Telefone)


class DadoAgenda:
    def __init__(self, nome: str) -> None:
        self.nome: str = nome
        self.telefones = Telefones()

    @property
    def nome(self) -> str:  # type: ignore
        return self.__nome  # type: ignore

    @nome.setter
    def nome(self, valor):  # type: ignore
        if not isinstance(valor, Nome):
            raise TypeError("nome deve ser uma instância da classe nome")
        self.__nome = valor

    def pesquisaTelefone(self, telefone):
        posicao = self.telefones.pesquisa(Telefone(telefone))
        if posicao == -1:
            return None
        else:
            return self.telefones[posicao]


class TiposTelefone(ListaUnica):
    def __init__(self) -> None:
        super().__init__(Tipotelefone)


class Agenda(ListaUnica):
    def __init__(self) -> None:
        super().__init__(DadoAgenda)
        self.tiposTelefone = TiposTelefone()

    def adicionaTipo(self, tipo):
        self.tiposTelefone.adiciona(Tipotelefone(tipo))

    def pesquisaNome(self, nome):
        if isinstance(nome, str):
            nome = Nome(nome)

        for dados in self.lista:
            if dados.nome == nome:
                return dados

        else:
            return None

    def ordena(self) -> None:  # type: ignore
        super().ordena(lambda dado: str(dado.nome))


def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return valor
        except ValueError:
            print(f"Valor invalido, favor digitar entre {inicio} e {fim}")


class Menu:
    def __init__(self) -> None:
        self.opcoes = [["sair", None]]

    def adiciona_opcao(self, nome, funcao):
        self.opcoes.append([nome, funcao])

    def exibe(self):
        print("====\nMenu\n=====\n")
        for i, opcao in enumerate(self.opcoes):
            print(f"[{i} - {opcao[0]}]")
        print()

    def execute(self):
        while True:
            self.exibe()
            escolha = valida_faixa_inteiro(
                "Escolha uma opcao: ", 0, len(self.opcoes) - 1
            )

            if escolha == 0:
                break
        self.opcoes[escolha][1]()
