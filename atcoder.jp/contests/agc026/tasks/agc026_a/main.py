N, *A = map(int, open(0).read().split())


ans = 0
for i in range(N - 1):
    if A[i] == A[i + 1]:
        ans += 1
        A[i + 1] = 10000


print(ans)
