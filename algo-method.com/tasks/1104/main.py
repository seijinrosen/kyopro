from itertools import groupby


def count_serial_char(s: str) -> "list[tuple[str, int]]":
    return [(k, len(list(g))) for k, g in groupby(s)]


N = int(input())
S = input()

counter = count_serial_char(S)
ans = 0

while 2 <= len(counter):
    k1, v1 = counter.pop()
    k2, v2 = counter[-1]
    counter[-1] = (k2, v1 + v2 + 1)
    ans += v1

print(ans)
