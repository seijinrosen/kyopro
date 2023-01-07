from typing import Tuple


def solve(n: int) -> Tuple[int, int]:
    for i in range(2, int(n ** (1 / 3)) + 1):
        if n % i != 0:
            continue
        if (n // i) % i == 0:
            return i, n // i // i
        return int((n // i) ** 0.5), i
    return 0, 0


T = int(input())
test_cases = [int(input()) for _ in range(T)]

for n in test_cases:
    p, q = solve(n)
    print(p, q)
