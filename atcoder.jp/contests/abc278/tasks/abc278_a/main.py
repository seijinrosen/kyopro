N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = A[K:] + [0] * min(N, K)
print(*ans)
