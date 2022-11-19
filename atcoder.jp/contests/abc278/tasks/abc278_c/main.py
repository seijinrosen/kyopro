from collections import defaultdict
from typing import DefaultDict, List, Set, Tuple

N, Q = map(int, input().split())
TAB: List[Tuple[int, int, int]] = [tuple(map(int, input().split())) for _ in range(Q)]

G: DefaultDict[int, Set[int]] = defaultdict(set)

for t, a, b in TAB:
    if t == 1:
        G[a].add(b)

    elif t == 2:
        G[a].discard(b)

    elif t == 3:
        ans = b in G[a] and a in G[b]
        print("Yes" if ans else "No")
