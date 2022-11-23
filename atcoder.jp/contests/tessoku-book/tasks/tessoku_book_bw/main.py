from operator import itemgetter
from typing import List, Tuple

N = int(input())
TD: List[Tuple[int, int]] = [tuple(map(int, input().split())) for _ in range(N)]

dp = [[0] * (max(d for _, d in TD) + 1)]
for t, d in sorted(TD, key=itemgetter(1)):
    dp.append(
        [max(p, dp[-1][j - t] + 1) if t <= j <= d else p for j, p in enumerate(dp[-1])]
    )

ans = max(dp[N])
print(ans)
