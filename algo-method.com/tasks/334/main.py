N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]


def solve() -> int:
    dp = [[0] * N for _ in range(N)]
    dp[0] = A[0]

    for i in range(N):
        for j in range(N):
            if j + 1 < N:
                dp[i][j + 1] = max(dp[i][j + 1], dp[i][j] + A[i][j + 1])
            if i + 1 < N:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + A[i + 1][j])

    return dp[N - 1][N - 1]


print(solve())
