N, *W = map(int, open(0).read().split())


def solve() -> int:
    total = sum(W)

    dp = [[False] * (total + 1) for _ in range(N + 1)]
    dp[0][0] = True

    for i in range(N):
        for j in range(total + 1):
            if not dp[i][j]:
                continue

            dp[i + 1][j + W[i]] = True
            dp[i + 1][abs(j - W[i])] = True

    return dp[N].index(True)


print(solve())
