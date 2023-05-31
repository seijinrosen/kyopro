N, M, *A = map(int, open(0).read().split())


def solve() -> int:
    dp = [0]

    for i in range(1, N):
        x = min(dp[i - m] + m * A[i] for m in range(1, min(i + 1, M + 1)))
        dp.append(x)

    return dp[N - 1]


print(solve())
