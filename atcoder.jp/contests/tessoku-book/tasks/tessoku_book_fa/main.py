from itertools import accumulate, starmap
from typing import List, Tuple

D = int(input())
A = [int(input()) for _ in range(D)]
Q = int(input())
ST: List[Tuple[int, int]] = [tuple(map(int, input().split())) for _ in range(Q)]

acc = [0, *accumulate(A)]


def func(s: int, t: int) -> str:
    if acc[s] == acc[t]:
        return "Same"
    return str(max(s, t, key=lambda x: acc[x]))


ans = starmap(func, ST)
print(*ans, sep="\n")
