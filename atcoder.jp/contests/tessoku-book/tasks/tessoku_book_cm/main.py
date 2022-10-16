from itertools import compress, product
from typing import Iterator, List, TypeVar

_T = TypeVar("_T")


def full_enumerate(lst: List[_T]) -> "Iterator[compress[_T]]":
    """全列挙"""
    for bits in product((0, 1), repeat=len(lst)):
        yield compress(lst, bits)


N, K = map(int, input().split())
A = list(map(int, input().split()))

P = map(sum, full_enumerate(A[: N // 2]))
Q = {*map(sum, full_enumerate(A[N // 2 :]))}

ans = any(K - p in Q for p in P)
print("Yes" if ans else "No")
