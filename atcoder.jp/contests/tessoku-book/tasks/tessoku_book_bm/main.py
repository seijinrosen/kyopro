from typing import List

N = int(input())
A = map(int, input().split())

G: List[List[int]] = [[] for _ in range(N)]
for i, a in enumerate(A, start=1):
    G[a - 1].append(i)

dp = [0] * N
for i in reversed(range(N)):
    dp[i] = sum(dp[j] + 1 for j in G[i])

print(*dp)
