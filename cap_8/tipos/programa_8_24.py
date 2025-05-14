# Programa 8.24: Diz o tipo de um parâmetro

import types


def diz_o_tipo(a):
    if isinstance(a, str):
        return "String"
    elif isinstance(a, list):
        return "Lista"
    elif isinstance(a, dict):
        return "Dicionário"
    elif isinstance(a, int):
        return "Número inteiro"
    elif isinstance(a, float):
        return "Número decimal"
    elif isinstance(a, types.FunctionType):
        return "Função"
    elif isinstance(a, types.BuiltinFunctionType):
        return "Função interna"
    else:
        return str(type(a))


print(diz_o_tipo(10))
print(diz_o_tipo(10.5))
print(diz_o_tipo("Alô"))
print(diz_o_tipo([1, 2, 3]))
print(diz_o_tipo({"a": 1, "b": 50}))
print(diz_o_tipo(print))
print(diz_o_tipo(None))
