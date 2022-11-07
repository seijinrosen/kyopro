N, K = map(int, input().split())
A = list(map(int, input().split()))

dp = [False] * (N + 1)
for i in range(N + 1):
    dp[i] = any(a <= i and not dp[i - a] for a in A)

print("First" if dp[N] else "Second")
