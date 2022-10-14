from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
X = [int(input()) for _ in range(Q)]

A.sort()
ans = [bisect_left(A, x) for x in X]

print(*ans, sep="\n")
