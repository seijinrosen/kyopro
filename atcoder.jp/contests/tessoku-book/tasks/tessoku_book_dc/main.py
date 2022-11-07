from functools import reduce
from math import factorial


def nCr(n: int, r: int, mod: int = 0) -> int:
    """組み合わせの数
    >>> nCr(4, 2)
    6
    >>> MOD = 10**9 + 7
    >>> nCr(4, 2, MOD)
    6
    >>> nCr(77777, 44444, MOD)
    409085577
    """
    if n < r:
        return 0
    if mod == 0:
        return factorial(n) // factorial(r) // factorial(n - r)

    def factorial_mod(x: int) -> int:
        return reduce(lambda a, i: a * i % mod, range(1, x + 1), 1)

    a = factorial_mod(n)
    b = factorial_mod(r) * factorial_mod(n - r)
    return a * pow(b, mod - 2, mod) % mod


H, W = map(int, input().split())

ans = nCr(H + W - 2, H - 1, 1000000007)
print(ans)
