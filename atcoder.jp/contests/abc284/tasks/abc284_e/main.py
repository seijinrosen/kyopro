import sys
from typing import List, Tuple

sys.setrecursionlimit(10**9)


def undirected_graph(n: int, uv: List[Tuple[int, int]]) -> List[List[int]]:
    g: list[list[int]] = [[] for _ in range(n)]
    for u, v in uv:
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)
    return g


N, M = map(int, input().split())
UV: List[Tuple[int, int]] = [tuple(map(int, input().split())) for _ in range(M)]

G = undirected_graph(N, UV)
visited = [False] * N
ans = 0


def dfs(v: int) -> None:
    global ans
    if 10**6 <= ans:
        return

    visited[v] = True
    ans += 1

    for nv in G[v]:
        if not visited[nv]:
            dfs(nv)

    visited[v] = False


dfs(0)
print(ans)
