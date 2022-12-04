N = int(input())


def func(x: float) -> float:
    return x * (x * (x + 1) + 2) + 3


lo = 0
hi = 100
while 0.001 < hi - lo:
    mid = (lo + hi) / 2
    if func(mid) < N:
        lo = mid
    else:
        hi = mid


print(lo)
