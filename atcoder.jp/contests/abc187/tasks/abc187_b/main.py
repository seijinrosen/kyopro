from itertools import combinations
from typing import List, Tuple

N = int(input())
XY: List[Tuple[int, int]] = [tuple(map(int, input().split())) for _ in range(N)]


ans = sum(
    -1 <= (y2 - y1) / (x2 - x1) <= 1 for (x1, y1), (x2, y2) in combinations(XY, 2)
)


print(ans)
