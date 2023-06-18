from typing import List

N, *P = map(int, open(0).read().split())


def solve() -> List[int]:
    j = N - 2
    while P[j] < P[j + 1]:
        j -= 1

    k = N - 1
    while P[j] < P[k]:
        k -= 1

    P[j], P[k] = P[k], P[j]

    return [*P[: j + 1], *P[:j:-1]]


print(*solve())
