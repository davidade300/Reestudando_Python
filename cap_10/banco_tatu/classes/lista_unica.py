from collections import (
    UserList,  # herda do tipo lista padrão mas expõe a lista interna
)

# em self.data, permitindo sobrescrever os metodos


class ListaUnica(UserList):
    def __init__(self, elem_clase, enumerable=None):
        super().__init__(enumerable)
        self.elem_classe = elem_clase

    def append(self, elem) -> None:  # type: ignore
        self.verifica_tipo(elem)

        if elem not in self.data:
            super().append(elem)

    def __setitem__(self, posicao, elem):
        self.verifica_tipo(elem)

        if elem not in self.data:
            super().__setitem__(posicao, elem)

    def verifica_tipo(self, elem):
        if not isinstance(elem, self.elem_classe):
            raise TypeError("tipo invalido")

    def extend(self, iteravel):  # type: ignore
        for elem in iteravel:
            self.append(elem)
