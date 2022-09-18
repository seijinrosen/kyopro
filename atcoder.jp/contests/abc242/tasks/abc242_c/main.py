N = int(input())

MOD = 998244353
dp = [[0] * 10 for _ in range(N)]
dp[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]


def plus_mod(x: int, y: int) -> int:
    return (x + y) % MOD


for i in range(N - 1):
    for x in range(1, 10):
        dp[i + 1][x] = plus_mod(dp[i + 1][x], dp[i][x])
        if x != 1:
            dp[i + 1][x - 1] = plus_mod(dp[i + 1][x - 1], dp[i][x])
        if x != 9:
            dp[i + 1][x + 1] = plus_mod(dp[i + 1][x + 1], dp[i][x])

ans = sum(dp[-1]) % MOD
print(ans)
