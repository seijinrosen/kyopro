N, M, *D = map(int, open(0).read().split())


def solve() -> bool:
    dp = [False] * (N + 1)
    dp[0] = True

    for i in range(N):
        if dp[i]:
            for d in D:
                if i + d <= N:
                    dp[i + d] = True

    return dp[N]


print("Yes" if solve() else "No")
