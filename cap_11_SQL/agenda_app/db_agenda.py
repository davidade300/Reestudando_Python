from ...cap_10.banco_tatu.classes.nome import Nome
from ...cap_10.banco_tatu.classes.telefone import Telefone, Tipotelefone
from ...cap_10.banco_tatu.lista_unica import ListaUnica


class DBListaUnica(ListaUnica):
    def __init__(self, elem_classe) -> None:
        super().__init__(elem_classe)
        self.apagados: list = []

    def remove(self, elem):
        if elem.id is not None:
            self.apagados.append(elem.id)
        super().remove(elem)

    def limpa(self):
        self.apagados: list = []


class DBNome(Nome):
    def __init__(self, nome: str, id_=None) -> None:
        super().__init__(nome)
        self.id = id_


class DBTipoTelefone(Tipotelefone):
    def __init__(self, id_, tipo) -> None:
        super().__init__(tipo)
        self.id = id_


class DBTelefone(Telefone):
    def __init__(
        self,
        numero: str,
        tipo: Tipotelefone | None = None,
        id_=None,
        id_nome=None,
    ) -> None:
        super().__init__(numero, tipo)
        self.id = id_
        self.id_nome = id_nome


class DBTelefones(DBListaUnica):
    def __init__(self) -> None:
        super().__init__(DBTelefone)


class DBTiposTelefone(ListaUnica):
    def __init__(self) -> None:
        super().__init__(DBTipoTelefone)


class DBDadoAgenda:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.telefones = DBTelefones()

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        if not isinstance(valor, DBNome):
            raise TypeError("nome deve ser uma instância da classe DBNome")

        self.__nome = valor

    def pesquisaTelefone(self, telefone):
        posicao: int = self.telefones.pesquisa(DBTelefone(telefone))

        if posicao == -1:
            return None
        else:
            return self.telefones[posicao]
