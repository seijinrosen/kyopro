N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


def solve() -> int:
    dp = [[-1] * M for _ in range(N)]
    dp[0][0] = 0

    for i in range(N - 1):
        for j in range(M):
            if dp[i][j] == -1:
                continue

            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            if j + A[i] < M:
                dp[i + 1][j + A[i]] = dp[i][j] + B[i]

    return dp[-1][-1]


print(solve())
