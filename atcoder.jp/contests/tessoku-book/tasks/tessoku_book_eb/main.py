from bisect import bisect, insort
from typing import List, Set, Tuple

Q = int(input())
QUERIES: List[Tuple[int, int]] = [tuple(map(int, input().split())) for _ in range(Q)]

st: Set[int] = set()
lst: List[int] = []

for q, x in QUERIES:
    if q == 1:
        if x not in st:
            st.add(x)
            insort(lst, x)

    elif q == 2:
        if not st:
            print(-1)
            continue
        if x in st:
            print(0)
            continue

        i = bisect(lst, x)

        if i == 0:
            ans = abs(x - lst[i])
        elif i == len(st):
            ans = abs(x - lst[i - 1])
        else:
            ans = min(abs(x - lst[i]), abs(x - lst[i - 1]))

        print(ans)
