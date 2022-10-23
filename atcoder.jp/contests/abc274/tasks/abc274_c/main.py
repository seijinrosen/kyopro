N = int(input())
A = list(map(int, input().split()))

k = [0] * (2 * N + 2)

for i, a in enumerate(A, start=1):
    k[2 * i] = k[a] + 1
    k[2 * i + 1] = k[a] + 1

for x in k[1:]:
    print(x)
