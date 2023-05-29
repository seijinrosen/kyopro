N = int(input())


def solve():
    dp = [1, 1]

    for i in range(2, N + 1):
        x = dp[i - 1] + dp[i - 2]
        dp.append(x)

    return dp[N]


print(solve())
