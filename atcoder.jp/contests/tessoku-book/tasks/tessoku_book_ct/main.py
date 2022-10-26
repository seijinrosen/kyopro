N = int(input())
S = input()

# dp[l][r]: l 文字目から r 文字目までの部分における最長回文の長さ (0-indexed)
dp = [[int(i == j) for j in range(N)] for i in range(N)]

# LEN = r - l
for LEN in range(1, N):
    for l in range(N - LEN):
        r = l + LEN
        dp[l][r] = max(
            dp[l][r - 1], dp[l + 1][r], dp[l + 1][r - 1] + 2 if S[l] == S[r] else 0
        )

ans = dp[0][N - 1]
print(ans)
