N, M, *W = map(int, open(0).read().split())


def solve() -> int:
    INF = 10**9

    dp = [[INF] * (M + 1) for _ in range(N + 1)]
    dp[0][0] = 0

    for i in range(N):
        for j in range(M + 1):
            if dp[i][j] == INF:
                continue

            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
            if j + W[i] <= M:
                dp[i + 1][j + W[i]] = dp[i][j] + 1

    if dp[N][M] == INF:
        return -1

    return dp[N][M]


print(solve())
