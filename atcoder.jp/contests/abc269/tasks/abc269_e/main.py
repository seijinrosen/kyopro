def send(a: int, b: int, c: int, d: int) -> int:
    print("?", a + 1, b + 1, c + 1, d + 1)
    return int(input())


N = int(input())

lo = 0
hi = N
while lo < hi:
    mid = (lo + hi) // 2
    if send(lo, mid, 0, N - 1) == mid - lo:
        hi = mid
    else:
        lo = mid + 1
X = lo

lo = 0
hi = N
while lo < hi:
    mid = (lo + hi) // 2
    if send(0, N - 1, lo, mid) == mid - lo:
        hi = mid
    else:
        lo = mid + 1
Y = lo

print("!", X + 1, Y + 1)
