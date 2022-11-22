from collections import deque
from math import inf
from typing import List, Tuple

N, M = map(int, input().split())
ABCD: List[Tuple[int, int, int, int]] = [
    tuple(map(int, input().split())) for _ in range(M)
]

G: List[List[Tuple[int, int, int]]] = [[] for _ in range(N)]
for a, b, c, d in ABCD:
    G[a - 1].append((b - 1, c, d))
    G[b - 1].append((a - 1, c, d))

dist: List[Tuple[float, int]] = [(inf, 0)] * N
dist[0] = 0, 0
que = deque([0])

while que:
    v = que.popleft()
    for nv, c, d in G[v]:
        if dist[nv][0] < dist[v][0] + c:
            continue
        dist[nv] = (
            (dist[nv][0], max(dist[nv][1], dist[v][1] + d))
            if dist[nv][0] == dist[v][0] + c
            else (dist[v][0] + c, dist[v][1] + d)
        )
        que.append(nv)

ans = dist[N - 1]
print(*ans)
