from itertools import product
from typing import List, Tuple

N = int(input())
A = list(map(int, input().split()))
S = [input() for _ in range(N)]
Q = int(input())
UV: List[Tuple[int, int]] = [
    tuple(int(x) - 1 for x in input().split()) for _ in range(Q)
]


INF = 10**9
dist = [[INF] * N for _ in range(N)]
vals = [[0] * N for _ in range(N)]


for i in range(N):
    dist[i][i] = 0


for i, s in enumerate(S):
    for j, ch in enumerate(s):
        if ch == "Y":
            dist[i][j] = 1
            vals[i][j] = A[j]


for k, i, j in product(range(N), repeat=3):
    if dist[i][j] > dist[i][k] + dist[k][j]:
        dist[i][j] = dist[i][k] + dist[k][j]
        vals[i][j] = vals[i][k] + vals[k][j]
    elif dist[i][j] == dist[i][k] + dist[k][j]:
        vals[i][j] = max(vals[i][j], vals[i][k] + vals[k][j])


for u, v in UV:
    if dist[u][v] == INF:
        print("Impossible")
    else:
        print(dist[u][v], vals[u][v] + A[u])
