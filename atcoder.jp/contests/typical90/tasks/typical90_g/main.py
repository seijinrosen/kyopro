from bisect import bisect

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
B = [int(input()) for _ in range(Q)]

A.sort()

for b in B:
    i = bisect(A, b) % N
    ans = min(abs(A[i] - b), abs(b - A[i - 1]))
    print(ans)
