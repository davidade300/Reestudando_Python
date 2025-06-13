from typing import Any, Iterator

from python_nilo_4ed.cap_10.banco_tatu.classes.clientes import Cliente


class ListaUnica:
    def __init__(self, elem_classe) -> None:
        self.lista: list = []
        self.elem_classe = elem_classe

    def __len__(self) -> int:
        return len(self.lista)

    def __iter__(self) -> Iterator[Any]:
        return iter(self.lista)

    def __getitem__(self, posicao: int) -> Any:
        return self.lista[posicao]

    def indiceValido(self, indice: int) -> bool:
        return indice >= 0 and indice < len(self.lista)

    def adiciona(self, elem: Cliente):
        if self.pesquisa(elem) == -1:
            self.lista.append(elem)

    def remove(self, elem: Cliente):
        self.lista.remove(elem)

    def pesquisa(self, elem: Cliente):
        self.verifica_tipo(elem)

        try:
            return self.lista.index(elem)
        except ValueError:
            return -1

    def verifica_tipo(self, elem: Cliente):
        if not isinstance(elem, self.elem_classe):
            raise TypeError("tipo invalido")

    def ordena(self, chave=None):
        self.lista.sort(key=chave)
