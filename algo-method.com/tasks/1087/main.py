from itertools import product
from typing import Iterator, Tuple


def bitset(n: int) -> Iterator[Tuple[int, ...]]:
    """bit 全探索"""
    for bits in product((0, 1), repeat=n):
        yield bits


def solve(bits: Tuple[int, ...]) -> int:
    stack: list[int] = []
    now = 1
    for i, op in enumerate(bits, 2):
        if op:
            now *= i
        else:
            stack.append(now)
            now = i
    return sum(stack) + now


N = int(input())
ans = N in map(solve, bitset(8))
print("Yes" if ans else "No")
