from functools import total_ordering

from lista_unica import ListaUnica

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

    def pesquisa(self, telefone: Telefone): ...  # FIXME:


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
