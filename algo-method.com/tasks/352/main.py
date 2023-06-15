N, A, B, *X = map(int, open(0).read().split())


def solve() -> bool:
    dp = [[False] * A for _ in range(N + 1)]
    dp[0][0] = True

    for i in range(N):
        for j in range(A):
            if not dp[i][j]:
                continue

            dp[i + 1][j] = True
            dp[i + 1][(j + X[i]) % A] = True

    return dp[N][B]


print("Yes" if solve() else "No")
