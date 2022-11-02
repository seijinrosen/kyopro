from bisect import bisect_left
from typing import Iterable, List


def lis(xs: Iterable[int]) -> int:
    """最長増加部分列 (Longest increasing subsequence)"""
    L: List[int] = []
    for x in xs:
        pos = bisect_left(L, x)
        if pos == len(L):
            L.append(x)
        else:
            L[pos] = x
    return len(L)


N = int(input())
A = list(map(int, input().split()))

ans = lis(A)
print(ans)
