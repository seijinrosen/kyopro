from collections import deque
from itertools import repeat
from operator import add
from typing import List, Tuple

INF = float("inf")

N, M = map(int, input().split())
ABC: List[Tuple[int, int, int]] = [tuple(map(int, input().split())) for _ in range(M)]

G: List[List[Tuple[int, int]]] = [[] for _ in range(N)]
for a, b, c in ABC:
    G[a - 1].append((b - 1, c))
    G[b - 1].append((a - 1, c))

dist = [INF] * N
dist[0] = 0
before = [-1] * N

que = deque([0])
while que:
    v = que.popleft()
    for nv, c in G[v]:
        if dist[v] + c < dist[nv]:
            dist[nv] = dist[v] + c
            before[nv] = v
            que.append(nv)

route = [N - 1]
while route[-1] != 0:
    route.append(before[route[-1]])

print(*map(add, repeat(1), reversed(route)))
