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

        ans: List[int] = []
        if 0 < i:
            ans.append(x - lst[i - 1])
        if i < len(lst):
            ans.append(lst[i] - x)

        print(min(ans))
