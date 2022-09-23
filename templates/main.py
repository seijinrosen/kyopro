from itertools import groupby, tee
from typing import Iterable, TypeVar

_T = TypeVar("_T")


def count_serial_char(s: str) -> "list[tuple[str, int]]":
    return [(k, len(list(g))) for k, g in groupby(s)]


def int2bin(number: int, width: int) -> str:
    return bin(number)[2:].zfill(width)


def is_odd(n: int) -> bool:
    return n % 2 == 1


def pairwise(iterable: Iterable[_T]) -> "zip[tuple[_T, _T]]":
    # https://docs.python.org/ja/3/library/itertools.html#itertools.pairwise
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def tails(s: str) -> "list[str]":
    return [s[i:] for i in range(len(s) + 1)]


def yes_no(b: bool) -> str:
    return "Yes" if b else "No"


N = int(input())
