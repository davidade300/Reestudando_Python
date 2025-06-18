class Contador:
    instancias = 0

    @classmethod
    def incrementa(cls):
        cls.instancias += 1


print(Contador.instancias)

Contador.incrementa()
Contador.incrementa()

print(Contador.instancias)
