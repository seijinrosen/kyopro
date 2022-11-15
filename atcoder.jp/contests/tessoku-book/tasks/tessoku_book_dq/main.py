N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())
QUERIES = [map(int, input().split()) for _ in range(Q)]

for q, x, y in QUERIES:
    x -= 1
    y -= 1

    if q == 1:
        A[x], A[y] = A[y], A[x]
    elif q == 2:
        print(A[x][y])
