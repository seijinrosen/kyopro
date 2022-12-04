from bisect import bisect_left

N, K = map(int, input().split())
A = sorted(map(int, input().split()))

ans = sum(N - bisect_left(A, K - a) for a in A)
print(ans)
