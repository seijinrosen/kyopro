from typing import Iterator, Tuple


def neighborhood(i: int, j: int, n: int = 4) -> Iterator[Tuple[int, int]]:
    x = (-1, 0, 0, 1)
    y = (0, -1, 1, 0)
    if n == 8:
        x = (-1, -1, -1, 0, 0, 1, 1, 1)
        y = (-1, 0, 1, -1, 1, -1, 0, 1)
    for di, dj in zip(x, y):
        yield i + di, j + dj


N, X = map(int, input().split())
grid = [[c == "#" for c in input()] for _ in range(N)]


def square(alive: bool, x: int) -> bool:
    if not alive and x == 3:
        return True
    if alive and x in {2, 3}:
        return True
    if alive and x <= 1:
        return False
    if alive and x >= 4:
        return False
    return alive


def calc_x(i: int, j: int) -> int:
    return sum(
        grid[ni][nj] for ni, nj in neighborhood(i, j, 8) if 0 <= ni < N if 0 <= nj < N
    )


for _ in range(X):
    grid = [[square(grid[i][j], calc_x(i, j)) for j in range(N)] for i in range(N)]


for row in grid:
    s = "".join("#" if b else "." for b in row)
    print(s)
