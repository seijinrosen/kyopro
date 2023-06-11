N, M, *W = map(int, open(0).read().split())


def solve() -> bool:
    dp = [{0} for _ in range(N + 1)]

    for i in range(N):
        for d in dp[i]:
            dp[i + 1].add(d)
            dp[i + 1].add(d + W[i])

    return M in dp[N]


print("Yes" if solve() else "No")
