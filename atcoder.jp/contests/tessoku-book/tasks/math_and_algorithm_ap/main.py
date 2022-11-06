N = int(input())

a = [0] * (N + 1)
a[1] = 1

for n in range(2, N + 1):
    a[n] = (a[n - 1] + a[n - 2]) % 1000000007

ans = a[N]
print(ans)
