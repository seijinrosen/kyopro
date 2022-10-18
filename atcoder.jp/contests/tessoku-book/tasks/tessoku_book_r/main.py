N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = [[True] + [False] * S]
for a in A:
    dp += [[dp[-1][j] or (a <= j and dp[-1][j - a]) for j in range(S + 1)]]

ans = dp[N][S]
print("Yes" if ans else "No")
