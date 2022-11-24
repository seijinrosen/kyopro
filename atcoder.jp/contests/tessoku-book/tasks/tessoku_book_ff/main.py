from operator import eq
from typing import List, Tuple

N = int(input())
ST: List[Tuple[str, str]] = [tuple(input().split()) for _ in range(N)]


def check(winning_number: str, s: str) -> str:
    if winning_number == s:
        return "1"
    if sum(map(eq, winning_number, s)) == 3:
        return "2"
    return "3"


candidates = [
    winning_number
    for winning_number in (str(i).zfill(4) for i in range(10000))
    if all(check(winning_number, s) == t for s, t in ST)
]

ans = candidates[0] if len(candidates) == 1 else "Can't Solve"
print(ans)
