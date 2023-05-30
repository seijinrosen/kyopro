N = int(input())


def solve():
    dp = [1, 1, 2]

    for i in range(3, N + 1):
        x = dp[i - 1] + dp[i - 2] + dp[i - 3]
        dp.append(x)

    return dp[N]


print(solve())
