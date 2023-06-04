N, *A = map(int, open(0).read().split())


def solve() -> int:
    dp = [A]

    for i in range(N - 1):
        dp.append(
            [
                sum(
                    [
                        dp[i][j - 1] if 0 <= j - 1 else 0,
                        dp[i][j],
                        dp[i][j + 1] if j + 1 < N else 0,
                    ]
                )
                % 100
                for j in range(N)
            ]
        )

    return dp[N - 1][N - 1]


print(solve())
