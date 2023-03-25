import sys
from functools import lru_cache

sys.setrecursionlimit(10**9)


X = int(input())
MOD = 998244353


@lru_cache()
def func(x: int) -> int:
    if x <= 4:
        return x
    return func(x // 2) * func((x + 1) // 2) % MOD


ans = func(X)


print(ans)
