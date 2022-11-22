from copy import deepcopy
from itertools import compress, product
from operator import itemgetter
from typing import Iterable, Iterator, List, Tuple, TypeVar

_T = TypeVar("_T")


def bitset(n: int) -> Iterator[Tuple[int, ...]]:
    """bit 全探索"""
    for bits in product((0, 1), repeat=n):
        yield bits


def count_2d(value: _T, table: Iterable[List[_T]]) -> int:
    return sum(row.count(value) for row in table)


def transpose(table: Iterable[Iterable[_T]]) -> List[List[_T]]:
    return list(map(list, zip(*table)))


H, W, K = map(int, input().split())
C = [list(input()) for _ in range(H)]

ans = 0

for bits in bitset(H):
    sum_bits = sum(bits)
    if K < sum_bits:
        continue

    grid = deepcopy(C)
    for i in compress(range(H), bits):
        grid[i] = ["#"] * W

    grid = transpose(grid)
    w = [row.count(".") for row in grid]
    ww = sorted(enumerate(w), key=itemgetter(1), reverse=True)

    for i, _ in ww[: K - sum_bits]:
        grid[i] = ["#"] * H

    ans = max(ans, count_2d("#", grid))

print(ans)
