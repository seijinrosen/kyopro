N, L, K, *A = map(int, open(0).read().split())


def pred(score: int) -> bool:
    k = 0
    now = 0
    for a in A:
        if score <= a - now and score <= L - a:
            k += 1
            now = a
    return K <= k


lo = 1
hi = L
while 1 < hi - lo:
    mid = (lo + hi) // 2
    if pred(mid):
        lo = mid
    else:
        hi = mid

print(lo)
