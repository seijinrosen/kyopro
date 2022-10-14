def f(x: float) -> float:
    return x**3 + x


N = int(input())

lo = 0
hi = N

while 0.0001 < hi - lo:
    mid = (lo + hi) / 2
    if f(mid) < N:
        lo = mid
    else:
        hi = mid

print(lo)
