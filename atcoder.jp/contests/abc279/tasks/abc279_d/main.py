A, B = map(int, input().split())


def fall_time(g: int) -> float:
    return A / g**0.5


lo = 1
hi = 10**18
while lo < hi:
    mid = (lo + hi) // 2
    if fall_time(mid + 1) + B < fall_time(mid):
        lo = mid + 1
    else:
        hi = mid

g = lo
ans = fall_time(g) + B * (g - 1)

print(ans)
