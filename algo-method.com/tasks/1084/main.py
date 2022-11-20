from itertools import compress, product
from typing import Iterator, Tuple


def bitset(n: int) -> Iterator[Tuple[int, ...]]:
    """bit 全探索"""
    for bits in product((0, 1), repeat=n):
        yield bits


N, M = map(int, input().split())
W = list(map(int, input().split()))
V = list(map(int, input().split()))

ans = max(sum(compress(V, bits)) for bits in bitset(N) if sum(compress(W, bits)) <= M)
print(ans)
