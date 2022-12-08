from itertools import tee
from typing import Iterable, TypeVar

_T = TypeVar("_T")


def pairwise(iterable: Iterable[_T]) -> "zip[tuple[_T, _T]]":
    # https://docs.python.org/ja/3/library/itertools.html#itertools.pairwise
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


N = int(input())
S = input()

MOD = 10**9 + 7
ATCODER = "atcoder"
ATCODER_SET = set(ATCODER)
PRE_CHAR = {y: x for x, y in pairwise(ATCODER)}

counter = {c: 0 for c in ATCODER}
for c in S:
    if c in ATCODER_SET:
        counter[c] += 1 if c == "a" else counter[PRE_CHAR[c]]
        counter[c] %= MOD

ans = counter["r"]
print(ans)
