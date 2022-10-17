N = int(input())
A = [0] * 2 + list(map(int, input().split()))
B = [0] * 3 + list(map(int, input().split()))

dp = [0] * (N + 1)
dp[2] = A[2]

for i in range(3, N + 1):
    dp[i] = min(dp[i - 1] + A[i], dp[i - 2] + B[i])

ans = dp[N]
print(ans)
