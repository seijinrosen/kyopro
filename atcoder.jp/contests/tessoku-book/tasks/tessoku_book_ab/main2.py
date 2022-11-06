from itertools import accumulate, islice
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


def func(p1: Pair, p2: Pair) -> Pair:
    _, a1 = p1
    t2, a2 = p2
    return t2, t2(a1, a2) % 10000


N = int(input())
TA = [input_pair() for _ in range(N)]

acc = accumulate(TA, func, initial=(add, 0))
ans = map(lambda t: t[1], islice(acc, 1, None))

print(*ans, sep="\n")
