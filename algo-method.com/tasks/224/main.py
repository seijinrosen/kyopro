import math

A, B = map(int, input().split())


def solve() -> int:
    return math.gcd(A, B)


print(solve())
