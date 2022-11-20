import sys
from typing import List, Tuple

sys.setrecursionlimit(10**9)


N, T = map(int, input().split())
AB: List[Tuple[int, int]] = [tuple(map(int, input().split())) for _ in range(N - 1)]

G: List[List[int]] = [[] for _ in range(N)]
for a, b in AB:
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

rank = [0] * N


def dfs(parent: int, i: int) -> int:
    for j in G[i]:
        if j != parent:
            rank[i] = max(rank[i], dfs(i, j) + 1)
    return rank[i]


dfs(-1, T - 1)
print(*rank)
