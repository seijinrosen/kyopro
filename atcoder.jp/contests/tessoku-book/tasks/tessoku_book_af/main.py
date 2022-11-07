N, A, B = map(int, input().split())

dp = [False] * (N + 1)
for i in range(N + 1):
    dp[i] = any(not dp[i - x] for x in [A, B] if x <= i)

print("First" if dp[N] else "Second")
