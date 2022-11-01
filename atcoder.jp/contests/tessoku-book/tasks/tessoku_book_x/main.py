from bisect import bisect_left
from typing import List

N = int(input())
A = list(map(int, input().split()))

L: List[int] = []

for a in A:
    pos = bisect_left(L, a)
    if pos < len(L):
        L[pos] = a
    else:
        L.append(a)

ans = len(L)
print(ans)
