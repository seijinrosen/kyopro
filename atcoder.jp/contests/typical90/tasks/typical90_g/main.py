from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
B = [int(input()) for _ in range(Q)]

A.sort()

for b in B:
    i = bisect_left(A, b, hi=N - 1)
    ans = min(abs(A[i] - b), abs(A[i - 1] - b))
    print(ans)
