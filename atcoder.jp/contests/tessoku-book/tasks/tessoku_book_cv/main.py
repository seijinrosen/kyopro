from itertools import product
from typing import List, Tuple

N = int(input())
XY: List[Tuple[int, int]] = [tuple(map(int, input().split())) for _ in range(N)]

# dp[既に訪問した都市の集合][今いる都市]
INF = float("inf")
dp = [[INF] * N for _ in range(2**N)]
dp[0][0] = 0


def dist(p: Tuple[int, int], q: Tuple[int, int]) -> float:
    x1, y1 = p
    x2, y2 = q
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


for i, j, k in product(range(2**N), range(N), range(N)):
    if (i // 2**k) % 2 == 0:
        dp[2**k + i][k] = min(dp[2**k + i][k], dp[i][j] + dist(XY[j], XY[k]))

ans = dp[-1][0]
print(ans)
