N, K = map(int, input().split())

n = N
for _ in range(K):
    n = n // 200 if n % 200 == 0 else int(str(n) + "200")

print(n)
