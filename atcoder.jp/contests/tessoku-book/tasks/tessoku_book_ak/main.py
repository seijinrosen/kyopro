N, M, B = map(int, input().split())
A = map(int, input().split())
C = map(int, input().split())

ans = sum(A) * M + sum(C) * N + B * N * M
print(ans)
