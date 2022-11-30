from itertools import product

H, W = map(int, input().split())
A, B = ([list(map(int, input().split())) for _ in range(H)] for _ in range(2))

ans = 0
for x in range(H - 1):
    for y in range(W - 1):
        d = B[x][y] - A[x][y]
        for i, j in product((0, 1), repeat=2):
            A[x + i][y + j] += d
        ans += abs(d)

if A == B:
    print("Yes")
    print(ans)
else:
    print("No")
