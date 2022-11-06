from itertools import accumulate
from operator import add, mul, sub
from typing import Callable, Tuple

BinaryOperator = Callable[[int, int], int]
Pair = Tuple[BinaryOperator, int]


def convert2operator(t: str) -> BinaryOperator:
    if t == "+":
        return add
    if t == "-":
        return sub
    return mul


def input_pair() -> Pair:
    t, a = input().split()
    return convert2operator(t), int(a)


def func(x: int, p: Pair) -> int:
    t, a = p
    return t(x, a) % 10000


N = int(input())
TA = [input_pair() for _ in range(N)]

ans = accumulate(TA, func, initial=0)
next(ans)

print(*ans, sep="\n")
