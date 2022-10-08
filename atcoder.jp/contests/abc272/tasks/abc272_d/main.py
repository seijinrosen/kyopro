from collections import deque
from itertools import product

N, M = map(int, input().split())

grid = [[-1] * N for _ in range(N)]
grid[0][0] = 0

d_list = [
    (i, j) for i, j in product(range(-400, 401), repeat=2) if i ** 2 + j**2 == M
]

que: "deque[tuple[int, int]]" = deque([(0, 0)])

while que:
    i, j = que.popleft()

    for di, dj in d_list:
        ni = i + di
        nj = j + dj
        if 0 <= ni < N and 0 <= nj < N and grid[ni][nj] == -1:
            que.append((ni, nj))
            grid[ni][nj] = grid[i][j] + 1

for g in grid:
    print(*g)
