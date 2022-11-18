from itertools import compress, product
from typing import Iterator, List, TypeVar

_T = TypeVar("_T")


def full_enumerate(lst: List[_T]) -> "Iterator[compress[_T]]":
    """全列挙"""
    for bits in product((0, 1), repeat=len(lst)):
        yield compress(lst, bits)


N, V = map(int, input().split())
A = list(map(int, input().split()))

ans = V in map(sum, full_enumerate(A))
print("Yes" if ans else "No")
