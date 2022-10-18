N = int(input())
H = [0, *map(int, input().split())]

dp = [0, 0] + [float("inf")] * (N - 1)

for i in range(1, N - 1):
    for j in [i + 1, i + 2]:
        dp[j] = min(dp[j], dp[i] + abs(H[i] - H[j]))

j = N
i = j - 1
dp[j] = min(dp[j], dp[i] + abs(H[i] - H[j]))

route = [j]

while 1 < j:
    i = j - 1
    if dp[i] + abs(H[i] - H[j]) == dp[j]:
        j -= 1
    else:
        j -= 2
    route.append(j)

ans = route[::-1]
print(len(ans))
print(*ans)
