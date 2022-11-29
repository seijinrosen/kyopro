from itertools import permutations, tee
from typing import Iterable, Set, Tuple, TypeVar

_T = TypeVar("_T")


def pairwise(iterable: Iterable[_T]) -> "zip[tuple[_T, _T]]":
    # https://docs.python.org/ja/3/library/itertools.html#itertools.pairwise
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
XY: Set[Tuple[int, int]] = {
    tuple(int(x) - 1 for x in input().split()) for _ in range(M)
}

ans = min(
    (
        sum(A[i][j] for j, i in enumerate(perm))
        for perm in permutations(range(N))
        if not any((x, y) in XY or (y, x) in XY for x, y in pairwise(perm))
    ),
    default=-1,
)

print(ans)
