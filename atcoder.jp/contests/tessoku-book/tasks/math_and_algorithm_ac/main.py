N, *A = map(int, open(0).read().split())

dp1 = [0] * (N + 1)
dp2 = [0] * (N + 1)

for i, a in enumerate(A, 1):
    dp1[i] = dp2[i - 1] + a
    dp2[i] = max(dp1[i - 1], dp2[i - 1])

ans = max(dp1[N], dp2[N])
print(ans)
