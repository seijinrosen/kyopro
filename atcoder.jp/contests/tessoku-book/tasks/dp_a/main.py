N = int(input())
H = [0] + list(map(int, input().split()))

INF = float("inf")
dp = [0, 0] + [INF] * (N - 1)

for i in range(1, N - 1):
    for j in [i + 1, i + 2]:
        dp[j] = min(dp[j], dp[i] + abs(H[i] - H[j]))

dp[N] = min(dp[N], dp[N - 1] + abs(H[N - 1] - H[N]))
ans = dp[N]

print(ans)
