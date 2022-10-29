from itertools import combinations
from typing import Tuple

S = [input() for _ in range(9)]


def dist(p: Tuple[int, int], q: Tuple[int, int]) -> int:
    x1, y1 = p
    x2, y2 = q
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


ans = 0
ps = [(x, y) for x in range(9) for y in range(9)]

for a, b, c, d in combinations(ps, 4):
    if (
        S[a[0]][a[1]] == "#"
        and S[b[0]][b[1]] == "#"
        and S[c[0]][c[1]] == "#"
        and S[d[0]][d[1]] == "#"
    ):
        if (
            dist(a, b) == dist(a, c)
            and dist(a, b) == dist(c, d)
            and dist(a, b) == dist(b, d)
            and dist(a, d) == dist(b, c)
        ):
            ans += 1

print(ans)
