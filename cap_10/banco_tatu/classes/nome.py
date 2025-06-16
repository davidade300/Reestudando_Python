class Nome:
    def __init__(self, nome: str) -> None:
        if nome is None or not nome.strip():
            raise ValueError("Nome não pode ser nulo nem em branco")
        self.nome = nome
        self.chave = nome.strip().lower()

    def __str__(self) -> str:
        return self.nome

    def __repr__(self) -> str:  # melhor que o da dio LOL (so adaptar)
        return f"<Classe {type(self).__name__} em 0x{id(self):x} Nome: {self.nome} Chave: {self.chave}>"

    def __eq__(self, other) -> bool:
        print("__eq__ chamado")

        return self.nome == other.nome

    def __lt__(self, other):  # less than
        print("__lt__ chamado")

        return self.nome < other.nome


d = Nome("David")
print(d)
print(d.__repr__())
