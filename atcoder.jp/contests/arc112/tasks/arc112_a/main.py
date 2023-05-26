from typing import List, Tuple

T = int(input())
LR: List[Tuple[int, int]] = [tuple(map(int, input().split())) for _ in range(T)]


def solve(l: int, r: int) -> int:
    n = r - l * 2
    if n < 0:
        return 0
    return (n + 1) * (n + 2) // 2


for l, r in LR:
    print(solve(l, r))
