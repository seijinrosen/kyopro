N, M = map(int, input().split())
W = list(map(int, input().split()))
V = list(map(int, input().split()))


def solve() -> int:
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(N):
        for j in range(M + 1):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            if j + W[i] <= M:
                dp[i + 1][j + W[i]] = dp[i][j] + V[i]

    return max(dp[N])


print(solve())
