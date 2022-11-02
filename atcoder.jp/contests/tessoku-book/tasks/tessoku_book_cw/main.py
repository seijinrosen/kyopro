from bisect import bisect_left
from typing import Iterable, List, Tuple


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
XY: List[Tuple[int, int]] = [tuple(map(int, input().split())) for _ in range(N)]

XY.sort(key=lambda xy: (xy[0], -xy[1]))
ans = lis(y for _, y in XY)

print(ans)
