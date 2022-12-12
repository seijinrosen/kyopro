import sys
from typing import List

sys.setrecursionlimit(10**9)


def func(n: int, l: int, r: int) -> List[str]:
    if l > r:
        return []
    if n == 0:
        return [""]
    return [str(l) + s for s in func(n - 1, l, r)] + func(n, l + 1, r)


L, R = map(int, input().split())

ans = sum(int(s) for s in func(10, 0, 9) if L <= int(s) <= R)
print(ans)
