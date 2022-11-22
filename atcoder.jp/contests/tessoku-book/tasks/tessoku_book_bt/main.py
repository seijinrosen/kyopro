from copy import deepcopy
from itertools import compress, product
from operator import itemgetter
from typing import Iterator, List, Tuple


def bitset(n: int) -> Iterator[Tuple[int, ...]]:
    """bit 全探索"""
    for bits in product((0, 1), repeat=n):
        yield bits


def transpose_str(table: List[str]) -> List[str]:
    return list(map("".join, zip(*table)))


H, W, K = map(int, input().split())
C = [input() for _ in range(H)]

ans = 0

for bits in bitset(H):
    sum_bits = sum(bits)
    if K < sum_bits:
        continue

    grid = deepcopy(C)
    for i in compress(range(H), bits):
        grid[i] = "#" * W

    grid = transpose_str(grid)
    w = [row.count(".") for row in grid]
    ww = sorted(enumerate(w), key=itemgetter(1), reverse=True)

    for i, _ in ww[: K - sum_bits]:
        grid[i] = "#" * H

    ans = max(ans, sum(row.count("#") for row in grid))

print(ans)
