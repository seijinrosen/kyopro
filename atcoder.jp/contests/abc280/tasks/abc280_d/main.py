from itertools import count, takewhile
from typing import Callable, Counter


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


def is_positive(n: int) -> bool:
    return 0 < n


def legendre(n: int, p: int) -> int:
    """ルジャンドルの公式: n! は 素数 p で何回割り切れるか"""
    return sum(takewhile(is_positive, (n // p**i for i in count(1))))


K = int(input())
prime_factors_K = prime_factorize(K)


def pred(n: int) -> bool:
    """n! は K の倍数か？"""
    return all(e <= legendre(n, p) for p, e in prime_factors_K.items())


def binary_search(lo: int, hi: int, pred: Callable[[int], bool]) -> int:
    while lo < hi:
        mid = (lo + hi) // 2
        if pred(mid):
            hi = mid
        else:
            lo = mid + 1
    return hi


ans = binary_search(2, K, pred)
print(ans)
