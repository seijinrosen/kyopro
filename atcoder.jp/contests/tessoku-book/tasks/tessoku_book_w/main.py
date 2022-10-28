import copy

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]

INF = 10**9
dp = [[INF] * (1 << N)]
dp[0][0] = 0

for t in (sum(2**i for i, b in enumerate(a) if b) for a in A):
    row = copy.copy(dp[-1])
    for s, p in enumerate(dp[-1]):
        v = s | t
        row[v] = min(row[v], p + 1)
    dp += [row]

ans = -1 if dp[M][-1] == INF else dp[M][-1]
print(ans)
