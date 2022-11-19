from collections import deque
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

que = deque([0])
while que:
    v = que.popleft()
    for nv, c in G[v]:
        if dist[v] + c < dist[nv]:
            dist[nv] = dist[v] + c
            que.append(nv)

for d in dist:
    print(-1 if d == INF else d)
