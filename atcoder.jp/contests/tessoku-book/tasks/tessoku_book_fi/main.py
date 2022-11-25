N, K, *A = map(int, open(0).read().split())

lo = 1e0
hi = 1e9

while 1e-6 < hi - lo:
    mid = (lo + hi) / 2
    if K <= sum(a // mid for a in A):
        lo = mid
    else:
        hi = mid

ans = [int(a / lo) for a in A]
print(*ans)
