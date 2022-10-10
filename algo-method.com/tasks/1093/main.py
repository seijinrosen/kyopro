INFO: "list[tuple[int, int, int, int]]" = [
    tuple(map(int, input().split())) for _ in range(30)
]


def to_minute(h: int, m: int) -> int:
    return 60 * h + m


def subtract_break_time(m: int) -> int:
    if m <= 360:
        return m
    if m <= 480:
        return m - 45
    else:
        return m - 60


def func(info: "tuple[int, int, int, int]") -> int:
    total_m = to_minute(info[2], info[3]) - to_minute(info[0], info[1])
    return subtract_break_time(total_m)


total_m = sum(map(func, INFO))

h = total_m // 60
m = total_m % 60

print(h, m)
