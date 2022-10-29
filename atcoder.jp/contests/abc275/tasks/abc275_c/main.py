from itertools import combinations, product
from typing import Tuple

S = [input() for _ in range(9)]


def dist(p: Tuple[int, int], q: Tuple[int, int]) -> int:
    x1, y1 = p
    x2, y2 = q
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


pawn_coordinates = [(i, j) for i, j in product(range(9), repeat=2) if S[i][j] == "#"]

ans = [
    (a, b, c, d)
    for a, b, c, d in combinations(pawn_coordinates, 4)
    if dist(a, b) == dist(b, d) == dist(d, c) == dist(c, a)
    if dist(a, d) == dist(b, c)
]

print(len(ans))
