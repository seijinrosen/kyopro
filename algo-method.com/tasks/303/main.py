N, *A = map(int, open(0).read().split())


def solve():
    dp = [0, A[1]]

    for i in range(2, N):
        x = min(dp[i - 1] + A[i], dp[i - 2] + 2 * A[i])
        dp.append(x)

    return dp[N - 1]


print(solve())
