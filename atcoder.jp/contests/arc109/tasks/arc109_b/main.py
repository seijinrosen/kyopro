def sum_of_arithmetic_progression(head: int, last: int, count: int) -> int:
    """等差数列の和"""
    return (head + last) * count // 2


N = int(input())

lo = 1
hi = N + 1
while hi - lo != 1:
    mid = (lo + hi) // 2
    if N + 1 < sum_of_arithmetic_progression(1, mid, mid):
        hi = mid
    else:
        lo = mid

ans = N - lo + 1
print(ans)
