# Função recursiva que calcula o maior divisor comum entre a e b em que a>b


def mdc(a: int, b: int):
    if b == 0:
        return a
    return mdc(a, a % b)


print(f"MDC 10 e 5 -->  {mdc(10, 5)}")
print(f"MDC 32 e 24 --> {mdc(32, 24)}")
print(f"MDC 5 e 3 -->   {mdc(5, 3)}")

# Função recursiva que calcula o menor multiplo comum entre a e b em que a>b


def mmc(a: int, b: int):
    return abs(a * b) / mdc(a, b)


print(f"MMC 10 e 5 -->  {mmc(10, 5)}")
print(f"MMC 32 e 24 --> {mmc(32, 24)}")
print(f"MMC 5 e 3 -->   {mmc(5, 3)}")
