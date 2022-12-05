N, K, *L = map(int, open(0).read().split())

lo = 0
hi = max(L)
while 1e-7 < hi - lo:
    mid = (lo + hi) / 2
    if K <= sum(l // mid for l in L):
        lo = mid
    else:
        hi = mid

print(lo)
