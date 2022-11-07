N, A, B = map(int, input().split())

dp = [False] * (N + 1)
for i in range(A, N + 1):
    dp[i] = not dp[i - A] or (B <= i and not dp[i - B])

print("First" if dp[N] else "Second")
