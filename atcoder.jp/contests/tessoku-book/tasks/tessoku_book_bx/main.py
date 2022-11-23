from bisect import bisect_left

N, W, L, R = map(int, input().split())
X = [0, *map(int, input().split()), W]

MOD = 10**9 + 7
dp = [1]
dp_sum = [1]

for x in X[1:]:
    pos_l = bisect_left(X, x - R) - 1
    pos_r = bisect_left(X, x - L + 1) - 1

    a = dp_sum[pos_r] if 0 <= pos_r else 0
    b = dp_sum[pos_l] if 0 <= pos_l else 0
    dp.append((a - b) % MOD)

    dp_sum.append((dp_sum[-1] + dp[-1]) % MOD)

print(dp[N + 1])
