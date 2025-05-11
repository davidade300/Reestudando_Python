# Programa 8.17: funcao lambda que recebe um valor e retorna o dobro dele
# Per PEP 8, you should "Always use a def statement instead of an assignment
# statement that binds a lambda expression directly to an identifier."

a = lambda x: x * 2  # noqa: E731
print(a(3))
