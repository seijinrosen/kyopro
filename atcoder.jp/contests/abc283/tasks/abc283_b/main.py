N = int(input())
A = list(map(int, input().split()))
Q = int(input())

for _ in range(Q):
    q = map(int, input().split())
    t = next(q)

    if t == 1:
        k, x = q
        A[k - 1] = x

    elif t == 2:
        k = next(q)
        print(A[k - 1])
