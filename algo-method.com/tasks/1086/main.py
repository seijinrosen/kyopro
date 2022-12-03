from copy import deepcopy
from itertools import product
from typing import Iterable, Iterator, Tuple


def bitset(n: int) -> Iterator[Tuple[int, ...]]:
    """bit 全探索"""
    for bits in product((0, 1), repeat=n):
        yield bits


def bitset_2d(h: int, w: int) -> Iterator[Tuple[Tuple[int, ...]]]:
    for bits in product(bitset(w), repeat=h):
        yield bits


def neighborhood(
    i: int, j: int, h: int, w: int, include_self: bool = False, n: int = 4
) -> Iterator[Tuple[int, int]]:
    x = (-1, 0, 0, 1)
    y = (0, -1, 1, 0)
    if n == 8:
        x = (-1, -1, -1, 0, 0, 1, 1, 1)
        y = (-1, 0, 1, -1, 1, -1, 0, 1)
    if include_self:
        yield i, j
    for di, dj in zip(x, y):
        ni, nj = i + di, j + dj
        if 0 <= ni < h and 0 <= nj < w:
            yield ni, nj


def sum_2d(table: Iterable[Iterable[int]]) -> int:
    return sum(map(sum, table))


H, W = map(int, input().split())
S = [[c == "#" for c in input()] for _ in range(H)]

for bits_2d in bitset_2d(H, W):
    grid = deepcopy(S)
    for i in range(H):
        for j in range(W):
            if bits_2d[i][j]:
                for ni, nj in neighborhood(i, j, H, W, True):
                    grid[ni][nj] = not grid[ni][nj]
    if sum_2d(grid) == 0:
        ans = True
        break
else:
    ans = False

print("Yes" if ans else "No")
