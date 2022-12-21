N, A, B = map(int, input().split())

b = min(5, N)
a = N - b
ans = B * b + A * a

print(ans)
