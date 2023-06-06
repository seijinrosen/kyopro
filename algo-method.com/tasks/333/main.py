N = int(input())
S = [input() for _ in range(N)]


def solve() -> int:
    dp = [[0] * N for _ in range(N)]
    dp[0][0] = 1

    for i in range(N):
        for j in range(N):
            if j + 1 < N and S[i][j + 1] != "#":
                dp[i][j + 1] += dp[i][j]
            if i + 1 < N and S[i + 1][j] != "#":
                dp[i + 1][j] += dp[i][j]

    return dp[N - 1][N - 1]


print(solve())
