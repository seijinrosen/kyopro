from itertools import takewhile

N, K = map(int, input().split())
A = list(map(int, input().split()))

dp = [0] * (N + 1)

for n in range(1, N + 1):
    dp[n] = max(n - dp[n - a] for a in takewhile(lambda a: a <= n, A))

ans = dp[N]
print(ans)
