from itertools import accumulate
from typing import Union


def bool2score(x: Union[bool, int]) -> int:
    """
    >>> bool2score(False)
    -1
    >>> bool2score(True)
    1
    >>> bool2score(0)
    -1
    >>> bool2score(1)
    1
    """
    return 2 * x - 1


def input_int_pair_list(n: int) -> "list[tuple[int, int]]":
    return [tuple(map(int, input().split())) for _ in range(n)]


N = int(input())
A = list(map(int, input().split()))
Q = int(input())
LR = input_int_pair_list(Q)


def convert(x: int) -> str:
    if 0 < x:
        return "win"
    if x < 0:
        return "lose"
    return "draw"


acc = [0, *accumulate(map(bool2score, A))]
ans = [convert(acc[r] - acc[l - 1]) for l, r in LR]


print(*ans, sep="\n")
