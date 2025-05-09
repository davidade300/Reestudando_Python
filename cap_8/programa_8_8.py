# Fibonacci recursivo com prints para rastrear


def fib(n):
    print(f"calculando fib {n}")
    if n <= 1:
        print(f"fib de {n} = {n}")
        return n
    else:
        print(
            f"  Fibonacci de {n} = fibonacci {n - 1} + fibonacci {n - 2} = ..."
        )
        resultado = fib(n - 1) + fib(n - 2)
        print(
            f"  Fibonacci de {n} = fibonacci {n - 1} + fibonacci {n - 2} = {resultado}"
        )
        return resultado


fib(5)
