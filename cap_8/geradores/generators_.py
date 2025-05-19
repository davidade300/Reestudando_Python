"""Iteradores são uma forma de acessar os elementos de uma lista ou estrutura de dados,
de forma a separar o acesso da representação interna da estrutura em si.

A funcao iter, cria um iterador. Iterador é um objet que trabalha com um protocolo de
acesso bem simples, respondendo a chamadas que retornam o próximo elemento da sequência
e geram uma excecao do tipo StopIteration quando não há mais elementos a retornar
"""


def gerador_de_numeros():  # gerador com sequencia infinita
    i = 0
    while True:
        yield i
        i += 1


""" o yield funciona da mesma forma que return, mas difere quanto a não terminar a função
 yield pode ser entendido como um return que suspende a execução da função, retornando um
 valor. Ao chamarmos novamente essa função, a execução continua de onde parou da última vez,
 e não a partir da primeira linha da função

"""


g = gerador_de_numeros()
print(next(g))


### Gerador cm sequencia finita
def gerador_fibonacci():
    p = 0
    s = 1

    while s < 10:
        yield s
        p, s = s, s + p


print([x for x in gerador_fibonacci()])

"""geradores são úteis ao implementar funções que guardam seu estado entre 
diversas chamadas. Esse recurso pode ser utilizado para retirar lógica com-
plexa de uma repetição, deixando o código mais simples e fácil de ler.
"""


### transformando um gerador finito em lista
def gerador_fibonacci_2(fim):
    p = 0
    s = 1

    while s < fim:
        yield s
        p, s = s, s + p


print(list(gerador_fibonacci_2(30)))


### Generator comprehensions
""" Pode ser criado da mesma forma que list comprehensions, basta substituir 
os colchetes por parênteses.

>>> [x for x in range(10) if x % 3 == 0] # list compreehension
>>> [0,3,6,9]

>>> (x for x in range(10) if x % 3 == 0) # generator comprehension
>>> for y in (x for x in range(10) if x % 3 == 0):  print(y)

"""
