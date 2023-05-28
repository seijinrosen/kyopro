N, X, Y = map(int, input().split())


def solve():
    dp = [X, Y]

    for i in range(2, N):
        a = (dp[i - 2] + dp[i - 1]) % 100
        dp.append(a)

    return dp[N - 1]


print(solve())
