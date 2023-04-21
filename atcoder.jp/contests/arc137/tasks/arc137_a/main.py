import math

L, R = map(int, input().split())


def solve() -> int:
    diff = R - L
    while True:
        for x in range(L, R - diff + 1):
            y = x + diff
            if math.gcd(x, y) == 1:
                return diff
        diff -= 1


print(solve())
