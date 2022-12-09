import sys
from typing import List

sys.setrecursionlimit(10**9)


def func(n: int, l: int, r: int) -> List[List[int]]:
    if l > r:
        return []
    if n == 0:
        return [[]]
    return [[l, *lst] for lst in func(n - 1, l, r)] + func(n, l + 1, r)


for lst in func(*map(int, input().split())):
    print(*lst)
