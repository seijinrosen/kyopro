N, K, M = map(int, input().split())
A = list(map(int, input().split()))

x = N * M - sum(A)
ans = -1 if K < x else max(x, 0)

print(ans)
