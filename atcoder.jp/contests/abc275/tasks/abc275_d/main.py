import sys
from functools import lru_cache

sys.setrecursionlimit(10**9)


N = int(input())


@lru_cache
def f(x: int) -> int:
    if x == 0:
        return 1
    return f(x // 2) + f(x // 3)


ans = f(N)
print(ans)
