N, *A = map(int, open(0).read().split())

dp1 = [0]
dp2 = [0]

for a in A:
    dp1.append(dp2[-1] + a)
    dp2.append(max(dp1[-2], dp2[-1]))

ans = max(dp1[N], dp2[N])
print(ans)
