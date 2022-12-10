from functools import reduce
from math import factorial


def division(a: int, b: int, mod: int) -> int:
    """a ÷ b を mod で割った余り"""
    return a * pow(b, mod - 2, mod) % mod


def nCr(n: int, r: int, mod: int = 0) -> int:
    """組み合わせの数"""
    if n < r:
        return 0
    if mod == 0:
        return factorial(n) // factorial(r) // factorial(n - r)

    def factorial_mod(x: int) -> int:
        return reduce(lambda a, i: a * i % mod, range(1, x + 1), 1)

    a = factorial_mod(n)
    b = factorial_mod(r) * factorial_mod(n - r)
    return division(a, b, mod)


N, L, R = map(int, input().split())

ans = nCr(R - L + 1, N)
print(ans)
