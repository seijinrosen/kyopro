from collections import deque
from math import inf
from typing import Iterable, List, Tuple


class Graph:
    nodes: List[List[Tuple[int, int]]]

    def __init__(self, n: int, edges: Iterable[Tuple[int, int, int]]) -> None:
        self.nodes = [[] for _ in range(n)]
        for u, v, w in edges:
            self.nodes[u].append((v, w))
            self.nodes[v].append((u, w))

    def dist_from(self, start: int) -> List[float]:
        dist = [inf] * len(self.nodes)
        dist[start] = 0
        que = deque([start])
        while que:
            v = que.popleft()
            for nv, w in self.nodes[v]:
                if dist[v] + w < dist[nv]:
                    dist[nv] = dist[v] + w
                    que.append(nv)
        return dist


N = int(input())
AB: List[Tuple[int, int]] = [tuple(map(int, input().split())) for _ in range(N - 1)]

dist = Graph(N, ((a - 1, b - 1, 1) for a, b in AB)).dist_from(0)
g1 = [i for i, d in enumerate(dist, 1) if d % 2 == 0]
g2 = [i for i, d in enumerate(dist, 1) if d % 2 == 1]

ans = max(g1, g2, key=len)[: N // 2]
print(*ans)
