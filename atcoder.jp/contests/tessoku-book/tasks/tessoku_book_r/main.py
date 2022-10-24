N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = [{0}]
for a in A:
    dp += [{j for j in range(S + 1) if j in dp[-1] or j - a in dp[-1]}]

ans = S in dp[N]
print("Yes" if ans else "No")
