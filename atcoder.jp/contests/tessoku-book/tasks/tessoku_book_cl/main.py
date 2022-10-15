from itertools import accumulate

N, K = map(int, input().split())
A = list(map(int, input().split()))

acc = [0, *accumulate(A)]
R = [0] * N

for i in range(N):
    if 0 < i:
        R[i] = R[i - 1]

    while R[i] < N and acc[R[i] + 1] - acc[i] <= K:
        R[i] += 1

ans = sum(r - i for i, r in enumerate(R))
print(ans)
