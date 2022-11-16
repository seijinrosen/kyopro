from bisect import bisect_left
from typing import List, Tuple

Q = int(input())
QUERIES: List[Tuple[int, int]] = [tuple(map(int, input().split())) for _ in range(Q)]

lst: List[int] = []

for q, x in QUERIES:
    i = bisect_left(lst, x)

    if q == 1:
        lst.insert(i, x)

    elif q == 2:
        lst.pop(i)

    elif q == 3:
        ans = lst[i] if i < len(lst) else -1
        print(ans)
