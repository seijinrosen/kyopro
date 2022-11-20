N, *A = map(int, open(0).read().split())

dp = [0] * N
for i, a in reversed(list(enumerate(A, start=1))):
    dp[a - 1] += dp[i] + 1

print(*dp)
