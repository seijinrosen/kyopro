from typing import Union


def yes_no(b: Union[bool, int]) -> str:
    return "Yes" if b else "No"


N, M = map(int, input().split())
W = list(map(int, input().split()))

dp = [[[False, False] for _ in range(M + 1)] for _ in range(N + 1)]
dp[0][0][0] = True

for i, w in enumerate(W):
    for j in range(M + 1):
        dp[i + 1][j][0] |= dp[i][j][0]
        dp[i + 1][j][1] |= dp[i][j][1]

        if j + w <= M:
            dp[i + 1][j + w][1] |= dp[i][j][0]
            dp[i + 1][j + w][0] |= dp[i][j][1]

ans = dp[N][M][1]
print(yes_no(ans))
