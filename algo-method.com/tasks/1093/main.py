from typing import List, Tuple

Info = Tuple[int, int, int, int]


def to_minute(h: int, m: int) -> int:
    return 60 * h + m


def subtract_break_time(m: int) -> int:
    if m <= 360:
        return m
    if m <= 480:
        return m - 45
    else:
        return m - 60


def func(info: Info) -> int:
    sh, sm, eh, em = info
    return subtract_break_time(to_minute(eh, em) - to_minute(sh, sm))


INFO: List[Info] = [tuple(map(int, input().split())) for _ in range(30)]

total_m = sum(map(func, INFO))

h = total_m // 60
m = total_m % 60

print(h, m)
