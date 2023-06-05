N = int(input())


def solve() -> int:
    dp = [[1] * N]

    for _ in range(N - 1):
        row = [dp[-1][0]]
        for j in range(1, N):
            row.append(dp[-1][j] + row[j - 1])
        dp.append(row)

    return dp[N - 1][N - 1]


print(solve())
