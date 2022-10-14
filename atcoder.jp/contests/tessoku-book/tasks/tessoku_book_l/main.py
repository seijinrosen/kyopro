N, K = map(int, input().split())
A = list(map(int, input().split()))

lo = 1
hi = 10**9

while lo < hi:
    mid = (lo + hi) // 2
    if sum(mid // a for a in A) >= K:
        hi = mid
    else:
        lo = mid + 1

print(lo)
