from collections import deque
from typing import Iterator, Tuple


def neighborhood(i: int, j: int) -> Iterator[Tuple[int, int]]:
    for di, dj in zip((-1, 0, 0, 1), (0, -1, 1, 0)):
        yield i + di, j + dj


R, C = map(int, input().split())
si, sj = (int(x) - 1 for x in input().split())
gi, gj = (int(x) - 1 for x in input().split())
G = [input() for _ in range(R)]

dist = [[-1] * C for _ in range(R)]
dist[si][sj] = 0

que = deque([(si, sj)])
while que:
    i, j = que.popleft()
    for ni, nj in neighborhood(i, j):
        if all((0 <= ni < R, 0 <= nj < C, G[ni][nj] == ".", dist[ni][nj] == -1)):
            dist[ni][nj] = dist[i][j] + 1
            que.append((ni, nj))

ans = dist[gi][gj]
print(ans)
