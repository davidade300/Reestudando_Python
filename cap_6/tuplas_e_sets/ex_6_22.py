"""
Programa para comparar duas listas.
A primeira lista deve ser considerada como a versão inicial e a segunda como a
versão após alterações. Utilizando operações com sets(conjuntos), o programa
imprime a lista de modificações entre as duas versões, listando:
    - Os elementos que não mudaram;
    - Os novos elementos;
    - Os elementos que foram removidos;

"""

lista: list = [1, 2, 3, 4, 5, 6]
lista_modificada: list = [1, 2, 4, 8, 10, 12]

print("elementos que não mudaram: " + str(set(lista) & set(lista_modificada)))
print("novo elementos: " + str(set(lista_modificada) - set(lista)))
print(
    "Elementos que foram removidos:" + str(set(lista) - set(lista_modificada))
)
