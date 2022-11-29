N, L = map(int, input().split())

MOD = 10**9 + 7
dp = [1]

for i in range(1, N + 1):
    dp.append((dp[-1] + (dp[i - L] if L <= i else 0)) % MOD)

print(dp[N])
