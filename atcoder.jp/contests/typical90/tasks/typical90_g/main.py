from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
B = [int(input()) for _ in range(Q)]

A.sort()

for b in B:
    i = bisect_left(A, b)
    ans = min(abs(A[j] - b) for j in [i - 1, i] if 0 <= j < N)
    print(ans)
