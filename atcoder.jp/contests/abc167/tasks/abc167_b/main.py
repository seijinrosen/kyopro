A, B, C, K = map(int, input().split())

a = min(A, K)
b = min(B, K - a)
c = K - a - b

ans = a - c
print(ans)
