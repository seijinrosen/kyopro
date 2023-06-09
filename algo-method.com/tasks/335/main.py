N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]


def solve() -> int:
    dp = [[10**9] * N for _ in range(N)]
    dp[0][-1] = A[0][-1]

    for i in range(N):
        for j in reversed(range(N)):
            if 0 <= j - 1:
                dp[i][j - 1] = min(dp[i][j - 1], dp[i][j] + A[i][j - 1])
            if i + 1 < N:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + A[i + 1][j])

    return dp[-1][0]


print(solve())
