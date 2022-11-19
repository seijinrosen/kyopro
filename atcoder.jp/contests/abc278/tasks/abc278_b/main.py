from typing import Tuple

H, M = map(int, input().split())


def to_str(i: int):
    if i < 10:
        return "0", str(i)
    return str(i)


def to_time(a: str, b: str, c: str, d: str) -> Tuple[int, int]:
    h, m = int(a + b), int(c + d)
    return h, m


def to_another_time(a: str, b: str, c: str, d: str) -> Tuple[int, int]:
    h, m = int(a + c), int(b + d)
    return h, m


def is_valid_time(h: int, m: int) -> bool:
    return h < 24 and m < 60


a, b = to_str(H)
c, d = to_str(M)

while True:
    another_time = to_another_time(a, b, c, d)
    if is_valid_time(*another_time):
        break

    h, m = to_time(a, b, c, d)
    if m <= 58:
        m += 1
        c, d = to_str(m)
    elif m == 59 and h <= 22:
        m = 0
        h += 1
        a, b = to_str(h)
        c, d = to_str(m)
    elif h == 23:
        h = 0
        m = 0
        a, b = to_str(h)
        c, d = to_str(m)


h, m = to_time(a, b, c, d)
print(h, m)
