from itertools import groupby


def count_serial_char(s: str) -> "list[tuple[str, int]]":
    return [(k, len(list(g))) for k, g in groupby(s)]


def is_odd(n: int) -> bool:
    return n % 2 == 1


S = input()
K = int(input())

counter = count_serial_char(S)
ans = sum(v // 2 for _, v in counter) * K

if len(counter) == 1 and is_odd(counter[0][1]):
    ans += K // 2
elif counter[0][0] == counter[-1][0]:
    if is_odd(counter[0][1]) and is_odd(counter[-1][1]):
        ans += K - 1

print(ans)
