import sys
from itertools import repeat
from operator import add
from typing import List

sys.setrecursionlimit(10**9)


N, M = map(int, input().split())

G: List[List[int]] = [[] for _ in range(N)]
for _ in range(M):
    a, b = (int(x) - 1 for x in input().split())
    G[a].append(b)
    G[b].append(a)


before = [-1] * N


def dfs(v: int) -> None:
    for nv in G[v]:
        if before[nv] == -1:
            before[nv] = v
            dfs(nv)


dfs(0)

route = [N - 1]
while route[-1] != 0:
    route.append(before[route[-1]])

ans = map(add, repeat(1), reversed(route))
print(*ans)
