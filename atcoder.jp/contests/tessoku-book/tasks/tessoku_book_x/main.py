from bisect import bisect_left
from typing import List

N = int(input())
A = list(map(int, input().split()))

ans = 0
L: List[int] = []

for a in A:
    pos = bisect_left(L, a)

    if ans <= pos:
        L.append(a)
        ans += 1
    else:
        L[pos] = a

print(ans)
