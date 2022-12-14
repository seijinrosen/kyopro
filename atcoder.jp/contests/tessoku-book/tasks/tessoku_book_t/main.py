S = input()
T = input()

N = len(S)
M = len(T)
dp = [[0] * (M + 1)]

for s in S:
    row = [0]
    for j, t in enumerate(T, start=1):
        row += [max(dp[-1][j], row[-1], dp[-1][j - 1] + 1 if s == t else 0)]
    dp += [row]

ans = dp[N][M]
print(ans)
