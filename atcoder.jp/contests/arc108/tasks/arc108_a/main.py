from math import floor, sqrt

S, P = map(int, input().split())


def solve() -> bool:
    return any(n * (S - n) == P for n in range(1, floor(sqrt(P)) + 1))


print("Yes" if solve() else "No")
