from itertools import combinations
from typing import List, Tuple

N = int(input())
TLR: List[Tuple[int, int, int]] = [tuple(map(int, input().split())) for _ in range(N)]


def normalize(t: int, l: int, r: int) -> Tuple[float, float]:
    if t == 2:
        return l, r - 0.5
    if t == 3:
        return l + 0.5, r
    if t == 4:
        return l + 0.5, r - 0.5
    return l, r


ans = 0
for (t1, l1, r1), (t2, l2, r2) in combinations(TLR, 2):
    (_, r1), (l2, _) = sorted((normalize(t1, l1, r1), normalize(t2, l2, r2)))
    if l2 <= r1:
        ans += 1


print(ans)
