import sys
from typing import List, Tuple

sys.setrecursionlimit(10**9)


N, M = map(int, input().split())
AB: List[Tuple[int, int]] = [tuple(map(int, input().split())) for _ in range(M)]

G: List[List[int]] = [[] for _ in range(N)]
for a, b in AB:
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

seen = [False] * N


def dfs(i: int) -> None:
    seen[i] = True
    for nex in G[i]:
        if not seen[nex]:
            dfs(nex)


dfs(0)
print("The graph is connected." if all(seen) else "The graph is not connected.")
