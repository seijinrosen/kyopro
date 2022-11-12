from collections import Counter
from functools import partial, reduce
from math import factorial


def nCr(n: int, r: int, mod: int = 0) -> int:
    if n < r:
        return 0
    if mod == 0:
        return factorial(n) // factorial(r) // factorial(n - r)

    def factorial_mod(x: int) -> int:
        return reduce(lambda a, i: a * i % mod, range(1, x + 1), 1)

    a = factorial_mod(n)
    b = factorial_mod(r) * factorial_mod(n - r)
    return a * pow(b, mod - 2, mod) % mod


N = int(input())
A = list(map(int, input().split()))

ans = sum(map(partial(nCr, r=3), Counter(A).values()))
print(ans)
