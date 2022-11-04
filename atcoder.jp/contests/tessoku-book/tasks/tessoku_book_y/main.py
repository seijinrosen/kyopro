H, W = map(int, input().split())
C = [input() for _ in range(H)]

dp = [[0] * (W + 1) for _ in range(H + 1)]
dp[1][1] = 1

for i in range(1, H + 1):
    for j in range(1, W + 1):
        if C[i - 1][j - 1] == "#":
            continue
        if i == 1 and j == 1:
            continue
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

ans = dp[H][W]
print(ans)
