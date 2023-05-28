from bisect import bisect_left

N, Q = map(int, input().split())
A = list(map(int, input().split()))
X = [int(input()) for _ in range(Q)]


A.sort()
ans = [N - bisect_left(A, x) for x in X]


print(*ans, sep="\n")
