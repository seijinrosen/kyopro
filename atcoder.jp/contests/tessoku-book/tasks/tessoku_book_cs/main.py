S = input()
T = input()

N = len(S)
M = len(T)
dp = [range(M + 1)]

for s in S:
    row = [dp[-1][0] + 1]
    for j, t in enumerate(T, start=1):
        row += [min(dp[-1][j] + 1, row[-1] + 1, dp[-1][j - 1] + (s != t))]
    dp += [row]

ans = dp[N][M]
print(ans)
