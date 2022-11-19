H, M = map(int, input().split())


def is_valid_time(h: int, m: int) -> bool:
    a, b = divmod(h, 10)
    c, d = divmod(m, 10)
    return a * 10 + c < 24 and b * 10 + d < 60


h, m = H, M

while not is_valid_time(h, m):
    m += 1
    if m == 60:
        h += 1
        m = 0
    if h == 24:
        h = 0

print(h, m)
