from collections import defaultdict
from typing import DefaultDict, List, Tuple

N, Q = map(int, input().split())
A = list(map(int, input().split()))
XK: List[Tuple[int, int]] = [tuple(map(int, input().split())) for _ in range(Q)]


d: DefaultDict[int, List[int]] = defaultdict(list)
for i, a in enumerate(A, 1):
    d[a].append(i)


for x, k in XK:
    lst = d.get(x)

    if lst is not None and k <= len(lst):
        print(lst[k - 1])
    else:
        print(-1)
