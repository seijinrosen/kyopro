from math import ceil, log2
from typing import Counter


def prime_factorize(n: int) -> Counter[int]:
    """素因数分解"""
    counter: Counter[int] = Counter()
    p = 2
    while p * p <= n:
        e = 0
        while n % p == 0:
            e += 1
            n //= p
        if e != 0:
            counter[p] = e
        p += 1
    if n != 1:
        counter[n] = 1
    return counter


N = int(input())

ans = ceil(log2(sum(prime_factorize(N).values())))
print(ans)
