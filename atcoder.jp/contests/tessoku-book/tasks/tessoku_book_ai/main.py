N = int(input())
A = list(map(int, input().split()))

dp = [[0] * i for i in range(1, N)]
dp.append(A)

for i in reversed(range(N - 1)):
    for j in range(i + 1):
        f = max if i % 2 == 0 else min
        dp[i][j] = f(dp[i + 1][j], dp[i + 1][j + 1])

ans = dp[0][0]
print(ans)
