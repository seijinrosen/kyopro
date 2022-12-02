from itertools import product
from math import inf
from typing import List, Tuple

N, M = map(int, input().split())
UVW: List[Tuple[int, int, int]] = [tuple(map(int, input().split())) for _ in range(M)]

dist = [inf] * N
dist[0] = 0

for _, (u, v, w) in product(range(M), UVW):
    dist[v] = min(dist[v], dist[u] + w)

for _, (u, v, w) in product(range(M), UVW):
    if dist[u] + w < dist[v]:
        dist[v] = -inf

ans = dist[N - 1]
if ans == inf:
    print("impossible")
else:
    print(ans)
