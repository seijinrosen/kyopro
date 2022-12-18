from collections import deque
from enum import Enum, auto
from typing import List, Tuple

N, M = map(int, input().split())
UV: List[Tuple[int, int]] = [tuple(map(int, input().split())) for _ in range(M)]


class Color(Enum):
    NONE = auto()
    BLACK = auto()
    WHITE = auto()


G: List[List[int]] = [[] for _ in range(N)]
for u, v in UV:
    G[u - 1].append(v - 1)
    G[v - 1].append(u - 1)

color = [Color.NONE] * N


def bfs(start_v: int) -> Tuple[int, int]:
    is_bipartite = True
    color[start_v] = Color.BLACK
    black_count, white_count = 1, 0
    que = deque([start_v])

    while que:
        v = que.popleft()
        for nv in G[v]:
            if color[nv] == color[v]:
                is_bipartite = False
            if color[nv] == Color.NONE:
                if color[v] == Color.BLACK:
                    color[nv] = Color.WHITE
                    white_count += 1
                else:
                    color[nv] = Color.BLACK
                    black_count += 1
                que.append(nv)

    return (black_count, white_count) if is_bipartite else (-1, -1)


ans = N * (N - 1) // 2 - M

for start_v in range(N):
    if color[start_v] == Color.NONE:
        black_count, white_count = bfs(start_v)
        if black_count == -1:
            ans = 0
            break
        ans -= black_count * (black_count - 1) // 2
        ans -= white_count * (white_count - 1) // 2

print(ans)
