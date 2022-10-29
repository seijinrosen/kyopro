from itertools import combinations
from typing import Tuple

S = [input() for _ in range(9)]


def dist(p: Tuple[int, int], q: Tuple[int, int]) -> int:
    x1, y1 = p
    x2, y2 = q
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


ans = [
    (a, b, c, d)
    for a, b, c, d in combinations(((x, y) for x in range(9) for y in range(9)), 4)
    if all(S[x][y] == "#" for x, y in (a, b, c, d))
    if dist(a, b) == dist(b, d) == dist(d, c) == dist(c, a)
    if dist(a, d) == dist(b, c)
]

print(len(ans))
