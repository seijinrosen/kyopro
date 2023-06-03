A0, A1, A2, A3 = map(int, input().split())


def solve() -> int:
    dp = [[A0, A1, A2, A3]]

    for i in range(3):
        row = [
            sum(
                [
                    dp[i][j - 1] if 0 <= j - 1 else 0,
                    dp[i][j],
                    dp[i][j + 1] if j + 1 < 4 else 0,
                ]
            )
            for j in range(4)
        ]
        dp.append(row)

    return dp[3][3]


print(solve())
