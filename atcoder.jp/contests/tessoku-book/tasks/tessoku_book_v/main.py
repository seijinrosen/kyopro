N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [-1] * (N + 1)
dp[1] = 0

for i, (a, b) in enumerate(zip(A, B), start=1):
    if dp[i] != -1:
        dp[a] = max(dp[a], dp[i] + 100)
        dp[b] = max(dp[b], dp[i] + 150)

ans = dp[N]
print(ans)
