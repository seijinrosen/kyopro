from collections import deque
from math import inf
from typing import List, Tuple

N, M = map(int, input().split())
ABC: List[Tuple[int, int, int]] = [tuple(map(int, input().split())) for _ in range(M)]

G: List[List[Tuple[int, int]]] = [[] for _ in range(N)]
for a, b, c in ABC:
    G[a - 1].append((b - 1, c))
    G[b - 1].append((a - 1, c))


def dist_from(start: int, graph: List[List[Tuple[int, int]]]) -> List[float]:
    dist = [inf] * len(graph)
    dist[start] = 0
    que = deque([start])
    while que:
        v = que.popleft()
        for nv, c in graph[v]:
            if dist[v] + c < dist[nv]:
                dist[nv] = dist[v] + c
                que.append(nv)
    return dist


dist_from1 = dist_from(0, G)
dist_fromN = dist_from(-1, G)

ans = sum(x + y == dist_fromN[0] for x, y in zip(dist_from1, dist_fromN))
print(ans)
