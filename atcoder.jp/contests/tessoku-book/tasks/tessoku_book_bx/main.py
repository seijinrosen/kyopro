from bisect import bisect_left, bisect_right

N, W, L, R = map(int, input().split())
X = [0, *map(int, input().split()), W]

MOD = 10**9 + 7
dp = [0, 1]

for x in X[1:]:
    dp.append((dp[-1] + dp[bisect_right(X, x - L)] - dp[bisect_left(X, x - R)]) % MOD)

ans = dp[-1] - dp[-2]
print(ans % MOD)
