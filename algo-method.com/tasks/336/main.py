N, M, *A = map(int, open(0).read().split())


def solve() -> int:
    dp = [[False] * M for _ in range(N)]
    dp[0][0] = True

    for i in range(N - 1):
        for j in range(M):
            if not dp[i][j]:
                continue

            dp[i + 1][j] = True
            if j + A[i] < M:
                dp[i + 1][j + A[i]] = True

    return sum(dp[-1])


print(solve())
