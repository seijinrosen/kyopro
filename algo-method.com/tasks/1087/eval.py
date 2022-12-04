from itertools import product
from typing import Iterator, Tuple


def bitset(n: int) -> Iterator[Tuple[int, ...]]:
    """bit 全探索"""
    for bits in product((0, 1), repeat=n):
        yield bits


def solve(bits: Tuple[int, ...]) -> int:
    ex = ["1"]
    for i, op in enumerate(bits, 2):
        ex.append("*" if op else "+")
        ex.append(str(i))
    return eval("".join(ex))


N = int(input())
ans = N in map(solve, bitset(8))
print("Yes" if ans else "No")
