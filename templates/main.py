from bisect import bisect_left
from collections import Counter
from decimal import ROUND_HALF_UP, Decimal
from functools import reduce
from itertools import accumulate, compress, groupby, islice, product, tee
from math import factorial, gcd
from operator import mul
from typing import Any, Callable, Iterable, Iterator, List, Tuple, TypeVar, Union

_T = TypeVar("_T")
_U = TypeVar("_U")


# more-itertools
def iterate(func: Callable[[_T], _T], start: _T) -> Iterator[_T]:
    # https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.iterate
    while True:
        yield start
        start = func(start)


def nth(iterable: Iterable[_T], n: int, default: _U = None) -> Union[_T, _U]:
    # https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.nth
    return next(islice(iterable, n, None), default)


# functions
def run_length_encoding(s: str) -> "list[tuple[str, int]]":
    return [(k, len(list(g))) for k, g in groupby(s)]


def accumulate_2d(table: "list[list[int]]") -> "list[list[int]]":
    acc = [[0, *accumulate(row)] for row in table]
    return transpose([[0, *accumulate(column)] for column in transpose(acc)])


def bin2int(b: str) -> int:
    return int(b, 2)


def bitset(n: int) -> Iterator[Tuple[int, ...]]:
    """bit 全探索"""
    for bits in product((0, 1), repeat=n):
        yield bits


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


def coordinate_compression(lst: List[Any], start: int = 0) -> List[int]:
    """座標圧縮
    >>> coordinate_compression([46, 80, 11, 77, 46], start=1)
    [2, 4, 1, 3, 2]
    >>> coordinate_compression([8, 100, 33, 12, 6, 1211])
    [1, 4, 3, 2, 0, 5]
    """
    d = {x: i for i, x in enumerate(sorted(set(lst)), start=start)}
    return [d[x] for x in lst]


def div_ceil(a: int, b: int) -> int:
    return (a + b - 1) // b


def eratosthenes(n: int) -> List[int]:
    """N 以下の素数
    >>> eratosthenes(20)
    [2, 3, 5, 7, 11, 13, 17, 19]
    """
    deleted = [False] * (n + 1)
    deleted[0] = deleted[1] = True
    for i in range(int(n**0.5) + 1):
        if deleted[i]:
            continue
        for j in range(i * 2, n + 1, i):
            deleted[j] = True
    return [i for i, b in enumerate(deleted) if not b]


def even(n: int) -> bool:
    return n % 2 == 0


def fst(x: Tuple[_T, Any]) -> _T:
    return x[0]


def full_enumerate(lst: List[_T]) -> "Iterator[compress[_T]]":
    """全列挙"""
    for bits in product((0, 1), repeat=len(lst)):
        yield compress(lst, bits)


def int2bin(number: int, width: int) -> str:
    return bin(number)[2:].zfill(width)


def odd(n: int) -> bool:
    return n % 2 == 1


def is_prime(x: int) -> bool:
    return all(x % i != 0 for i in range(2, int(x**0.5) + 1))


def is_same_parity(x: int, y: int) -> bool:
    return x % 2 == y % 2


def lcm(x: int, y: int) -> int:
    """最小公倍数 (least common multiple)
    >>> lcm(25, 30)
    150
    >>> lcm(998244353, 998244853)
    996492287418565109
    """
    return x // gcd(x, y) * y


def lis(xs: Iterable[int]) -> int:
    """最長増加部分列 (Longest increasing subsequence) の長さ
    >>> lis([2, 3, 1, 6, 4, 5])
    4
    >>> lis([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    1
    >>> lis([30, 50, 60, 10, 20])
    3
    >>> lis([90, 80, 70, 60, 50, 40, 30, 20, 10])
    1
    """
    L: List[int] = []
    for x in xs:
        pos = bisect_left(L, x)
        if pos == len(L):
            L.append(x)
        else:
            L[pos] = x
    return len(L)


def nCr(n: int, r: int, mod: int = 0) -> int:
    """組み合わせの数
    >>> nCr(4, 2)
    6
    """
    if n < r:
        return 0
    a = factorial(n)
    b = factorial(r) * factorial(n - r)
    if mod == 0:
        return a // b
    return a * pow(b, mod - 2, mod) % mod


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


def prod(iterable: Iterable[int]) -> int:
    return reduce(mul, iterable)


def round_half_up(number: int, ndigits: int) -> int:
    """四捨五入
    参考: https://note.nkmk.me/python-round-decimal-quantize/
    >>> round_half_up(2048, -1)
    2050
    >>> round_half_up(2050, -2)
    2100
    >>> round_half_up(1, -1)
    0
    >>> round_half_up(999, -1)
    1000
    """
    return int(
        Decimal(number).quantize(Decimal(f"1E{-ndigits}"), rounding=ROUND_HALF_UP)
    )


def snd(x: Tuple[Any, _T]) -> _T:
    return x[1]


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
Pair = Tuple[int, int]
Triple = Tuple[int, int, int]
input_int_list = lambda: list(map(int, input().split()))


def input_pair() -> Tuple[str, str]:
    return tuple(input().split())


def input_int_tuple_list(n: int) -> List[Tuple[int, int]]:
    return [tuple(map(int, input().split())) for _ in range(n)]


# N = int(input())
# A = list(map(int, input().split()))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
