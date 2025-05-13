# fibonacci não recursivo


def fib(n):
    p = 0
    s = 1

    while n > 0:
        p, s = s, s + p
        n -= 1
    return p


for x in range(10):
    print(f"fib({x}) = {fib(x)}")
