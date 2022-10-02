from itertools import groupby, tee
from typing import Iterable, Iterator, TypeVar, Union

_T = TypeVar("_T")


def run_length_encoding(s: str) -> "list[tuple[str, int]]":
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


def sum_of_arithmetic_progression(head: int, last: int, count: int) -> int:
    """等差数列の和"""
    return (head + last) * count // 2


def tails(s: str) -> "list[str]":
    return [s[i:] for i in range(len(s) + 1)]


def yes_no(b: Union[bool, int]) -> str:
    return "Yes" if b else "No"


def input_ints() -> Iterator[int]:
    for i in map(int, input().split()):
        yield i


def input_int_list() -> "list[int]":
    return list(map(int, input().split()))


N = int(input())
