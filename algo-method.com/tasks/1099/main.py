def mod_index1(x: int, y: int) -> int:
    """
    >>> mod_index1(1, 7)
    1
    >>> mod_index1(6, 7)
    6
    >>> mod_index1(7, 7)
    7
    >>> mod_index1(8, 7)
    1
    >>> mod_index1(13, 7)
    6
    >>> mod_index1(14, 7)
    7
    >>> mod_index1(15, 7)
    1
    """
    return (x - 1) % y + 1


A, B, C = map(int, input().split())
Y0, M0, D0, X = map(int, input().split())
Y1, M1, D1 = map(int, input().split())


def days_from_base_day(y: int, m: int, d: int) -> int:
    return A * B * (y - 1) + B * (m - 1) + d - 1


d0 = days_from_base_day(Y0, M0, D0)
d1 = days_from_base_day(Y1, M1, D1)

diff = d1 - d0
ans = mod_index1(X + diff, C)

print(ans)
