N, K = map(int, input().split())
A = list(map(int, input().split()))

dp = [False] * (N + 1)
for i in range(N + 1):
    dp[i] = any(not dp[i - a] for a in A if a <= i)

print("First" if dp[N] else "Second")
