N, K = map(int, input().split())
A = list(map(int, input().split()))

R = [0] * (N - 1)

for i in range(N - 1):
    if 0 < i:
        R[i] = R[i - 1]

    while R[i] < N - 1 and A[R[i] + 1] - A[i] <= K:
        R[i] += 1

ans = sum(r - i for i, r in enumerate(R))
print(ans)
