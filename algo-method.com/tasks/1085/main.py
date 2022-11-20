from itertools import compress, product
from typing import Iterable, Iterator, Tuple


def bitset(n: int) -> Iterator[Tuple[int, ...]]:
    """bit 全探索"""
    for bits in product((0, 1), repeat=n):
        yield bits


def is_pangram(words: Iterable[str]) -> bool:
    return len(set("".join(words))) == 26


N = int(input())
W = input().split()

ans = min(
    (sum(bits) for bits in bitset(N) if is_pangram(compress(W, bits))), default=-1
)

print(ans)
