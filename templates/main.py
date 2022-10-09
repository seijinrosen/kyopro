from collections import Counter
from itertools import accumulate, groupby, tee
from typing import Iterable, TypeVar, Union

_T = TypeVar("_T")


def run_length_encoding(s: str) -> "list[tuple[str, int]]":
    return [(k, len(list(g))) for k, g in groupby(s)]


def accumulate_2d(table: "list[list[int]]") -> "list[list[int]]":
    acc = [[0, *accumulate(row)] for row in table]
    return transpose([[0, *accumulate(column)] for column in transpose(acc)])


def bin2int(b: str) -> int:
    return int(b, 2)


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


def even(n: int) -> bool:
    return n % 2 == 0


def int2bin(number: int, width: int) -> str:
    return bin(number)[2:].zfill(width)


def odd(n: int) -> bool:
    return n % 2 == 1


def is_same_parity(x: int, y: int) -> bool:
    return x % 2 == y % 2


def pairwise(iterable: Iterable[_T]) -> "zip[tuple[_T, _T]]":
    # https://docs.python.org/ja/3/library/itertools.html#itertools.pairwise
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def prime_factorize(n: int) -> "Counter[int]":
    """素因数分解"""
    counter: Counter[int] = Counter()
    p = 2
    while p * p <= n:
        e = 0
        while n % p == 0:
            e += 1
            n //= p
        if e != 0:
            counter[p] = e
        p += 1
    if n != 1:
        counter[n] = 1
    return counter


def sum_of_arithmetic_progression(head: int, last: int, count: int) -> int:
    """等差数列の和"""
    return (head + last) * count // 2


def sum_of_each_digit(i: int) -> int:
    return sum(map(int, str(i)))


def tails(s: str) -> "list[str]":
    return [s[i:] for i in range(len(s) + 1)]


def transpose(table: "list[list[_T]]") -> "list[list[_T]]":
    return list(map(list, zip(*table)))


def yes_no(b: Union[bool, int]) -> str:
    return "Yes" if b else "No"


# input functions --------------------------------------------------------------
def input_int_list() -> "list[int]":
    return list(map(int, input().split()))


def input_int_pair_list(n: int) -> "list[tuple[int, int]]":
    return [tuple(map(int, input().split())) for _ in range(n)]


def input_int_tuple_list(n: int) -> "list[tuple[int, int, int]]":
    return [tuple(map(int, input().split())) for _ in range(n)]


N = int(input())


ans = N


print(ans)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
