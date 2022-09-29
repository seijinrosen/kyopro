N, K = map(int, input().split())
X = list(map(int, input().split()))


def func(min_dist: int) -> bool:
    k = 1
    now = X[0]
    for x in X[1:]:
        if min_dist <= x - now:
            k += 1
            if k == K:
                return True
            now = x
    return False


lo = 1
hi = 10**10
while hi - lo > 1:
    mid = (hi + lo) // 2
    if func(mid):
        lo = mid
    else:
        hi = mid

ans = lo
print(ans)
