import sys
from bisect import bisect_left
from collections import deque
from decimal import ROUND_HALF_UP, Decimal
from functools import reduce
from itertools import accumulate, combinations, compress, groupby, islice, product, tee
from math import factorial, gcd, inf
from operator import itemgetter, mul, xor
from typing import (
    Any,
    Callable,
    Counter,
    Iterable,
    Iterator,
    List,
    Set,
    Tuple,
    TypeVar,
    Union,
)

sys.setrecursionlimit(10**9)
_T = TypeVar("_T")
_S = TypeVar("_S")
_U = TypeVar("_U")


class UnionFind:
    # https://algo-method.com/descriptions/136
    def __init__(self, n: int) -> None:
        self.par = [-1] * n
        self.rank = [0] * n
        self.siz = [1] * n
        self.group = n

    def root(self, x: int) -> int:
        if self.par[x] == -1:
            return x
        self.par[x] = self.root(self.par[x])
        return self.par[x]

    def is_same(self, x: int, y: int) -> bool:
        return self.root(x) == self.root(y)

    def unite(self, x: int, y: int) -> bool:
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.par[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        self.siz[rx] += self.siz[ry]
        self.group -= 1
        return True

    def size(self, x: int) -> int:
        return self.siz[self.root(x)]

    def kruskal(
        self, edges: Iterable[Tuple[int, int, int]], already_sorted: bool = False
    ) -> int:
        """クラスカル法: 最小全域木 (Minimum spanning tree) の重みの総和"""
        if not already_sorted:
            edges = sorted(edges, key=itemgetter(2))
        return sum(w for u, v, w in edges if self.unite(u, v))

    def kruskal2(
        self, edges: Iterable[Tuple[int, int, int]]
    ) -> Tuple[List[Tuple[int, int, int]], int]:
        """クラスカル法: 最小全域木 (Minimum spanning tree) を構成する辺の一例と重みの総和"""
        mst_edges = [(u, v, w) for u, v, w in edges if self.unite(u, v)]
        return mst_edges, sum(map(itemgetter(2), mst_edges))


# more-itertools
def iterate(func: Callable[[_T], _T], start: _T) -> Iterator[_T]:
    # https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.iterate
    while True:
        yield start
        start = func(start)


def nth(iterable: Iterable[_T], n: int, default: _U = None) -> Union[_T, _U]:
    # https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.nth
    return next(islice(iterable, n, None), default)


def triplewise(iterable: Iterable[_T]) -> Iterator[Tuple[_T, _T, _T]]:
    # https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.triplewise
    for (a, _), (b, c) in pairwise(pairwise(iterable)):
        yield a, b, c


# functions
def run_length_encoding(s: str) -> List[Tuple[str, int]]:
    """ランレングス圧縮"""
    return [(k, len(list(g))) for k, g in groupby(s)]


def accumulate_2d(table: "list[list[int]]") -> "list[list[int]]":
    acc = [[0, *accumulate(row)] for row in table]
    return transpose([[0, *accumulate(column)] for column in transpose(acc)])


def accumulate_initial(
    iterable: Iterable[_S], func: Callable[[_T, _S], _T], *, initial: _T
) -> Iterator[_T]:
    # https://docs.python.org/ja/3/library/itertools.html#itertools.accumulate
    total = initial
    yield total
    for element in iter(iterable):
        total = func(total, element)
        yield total


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


def constant_factory(value: _T) -> Callable[[], _T]:
    return lambda: value


def coordinate_compression(lst: List[Any], start: int = 0) -> List[int]:
    """座標圧縮
    >>> coordinate_compression([46, 80, 11, 77, 46], start=1)
    [2, 4, 1, 3, 2]
    >>> coordinate_compression([8, 100, 33, 12, 6, 1211])
    [1, 4, 3, 2, 0, 5]
    """
    d = {x: i for i, x in enumerate(sorted(set(lst)), start=start)}
    return [d[x] for x in lst]


def count_2d(value: _T, table: Iterable[List[_T]]) -> int:
    return sum(row.count(value) for row in table)


def diff(iterable: Iterable[int]) -> Iterator[int]:
    return (y - x for x, y in pairwise(iterable))


def dist_from(start: int, graph: List[List[Tuple[int, int]]]) -> List[float]:
    dist = [inf] * len(graph)
    dist[start] = 0
    que = deque([start])
    while que:
        v = que.popleft()
        for nv, c in graph[v]:
            if dist[v] + c < dist[nv]:
                dist[nv] = dist[v] + c
                que.append(nv)
    return dist


def div_ceil(a: int, b: int) -> int:
    return (a + b - 1) // b


def division(a: int, b: int, mod: int) -> int:
    """a ÷ b を mod で割った余り"""
    return a * pow(b, mod - 2, mod) % mod


def divisors(n: int) -> List[int]:
    """約数列挙
    >>> divisors(12)
    [1, 2, 3, 4, 6, 12]
    >>> divisors(827847039317)
    [1, 909859, 909863, 827847039317]
    """
    res: list[int] = []
    for i in range(1, n + 1):
        if n < i * i:
            break
        if n % i == 0:
            res.append(i)
            if i * i != n:
                res.append(n // i)
    return sorted(res)


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


def int2base(number: int, base: int) -> str:
    d = {2: bin, 8: oct, 16: hex}
    if base in d:
        return d[base](number)[2:]
    if number == 0:
        return "0"

    def f(n: int, b: int) -> str:
        if n == 0:
            return ""
        return f(n // b, b) + str(n % b)

    return f(number, base)


def int2bin(number: int, width: int) -> str:
    return bin(number)[2:].zfill(width)


def int2bitset(n: int) -> Set[int]:
    """
    https://algo-method.com/tasks/1082
    >>> int2bitset(13)
    {0, 2, 3}
    >>> int2bitset(1)
    {0}
    """
    return {i for i, x in enumerate(reversed(bin(n)[2:])) if x == "1"}


def inversion(iterable: Iterable[int]) -> int:
    """転倒数
    >>> inversion([2, 3, 4, 1])
    3
    >>> inversion([3, 1, 2, 4])
    2
    """
    return sum(y < x for x, y in combinations(iterable, 2))


def odd(n: int) -> bool:
    return n % 2 == 1


def is_natural(n: int) -> bool:
    return 0 <= n


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


def mex(st: Set[int]) -> int:
    """集合 st に含まれない最小の非負整数 (minimum excluded value)
    >>> mex({})
    0
    >>> mex({1})
    0
    >>> mex({0, 2})
    1
    >>> mex({0, 1, 3})
    2
    >>> mex({0, 1, 2})
    3
    """
    return next(i for i in range(len(st) + 1) if i not in st)


def mod_index1(x: int, y: int) -> int:
    """
    >>> mod_index1(1, 7)
    1
    >>> mod_index1(6, 7)
    6
    >>> mod_index1(7, 7)
    7
    >>> mod_index1(8, 7)
    1
    >>> mod_index1(13, 7)
    6
    >>> mod_index1(14, 7)
    7
    >>> mod_index1(15, 7)
    1
    """
    return (x - 1) % y + 1


def nCr(n: int, r: int, mod: int = 0) -> int:
    """組み合わせの数
    >>> nCr(4, 2)
    6
    >>> MOD = 10**9 + 7
    >>> nCr(4, 2, MOD)
    6
    >>> nCr(77777, 44444, MOD)
    409085577
    """
    if n < r:
        return 0
    if mod == 0:
        return factorial(n) // factorial(r) // factorial(n - r)

    def factorial_mod(x: int) -> int:
        return reduce(lambda a, i: a * i % mod, range(1, x + 1), 1)

    a = factorial_mod(n)
    b = factorial_mod(r) * factorial_mod(n - r)
    return division(a, b, mod)


def neighborhood(i: int, j: int, n: int = 4) -> Iterator[Tuple[int, int]]:
    x = (-1, 0, 0, 1)
    y = (0, -1, 1, 0)
    if n == 8:
        x = (-1, -1, -1, 0, 0, 1, 1, 1)
        y = (-1, 0, 1, -1, 1, -1, 0, 1)
    for di, dj in zip(x, y):
        yield i + di, j + dj


def nim(iterable: Iterable[int]) -> bool:
    """ニム和を計算し、先手必勝なら True を返す。
    >>> nim([7, 7])
    False
    >>> nim([5, 8])
    True
    """
    return 0 < reduce(xor, iterable)


def pairwise(iterable: Iterable[_T]) -> "zip[tuple[_T, _T]]":
    # https://docs.python.org/ja/3/library/itertools.html#itertools.pairwise
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def prime_factorize(n: int) -> Counter[int]:
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


def prod(iterable: Iterable[int], *, start: int = 1, mod: int = 0) -> int:
    if mod:
        return reduce(lambda a, b: a * b % mod, iterable, start)
    return reduce(mul, iterable, start)


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


def sum_of_arithmetic_progression(head: int, last: int, n: int = 0) -> int:
    """等差数列の和"""
    if n == 0:
        # 公差 d = 1 の場合、項数 n は省略可
        n = last - head + 1
    return n * (head + last) // 2


def sum_of_each_digit(i: int) -> int:
    return sum(map(int, str(i)))


def tails(s: str) -> "list[str]":
    return [s[i:] for i in range(len(s) + 1)]


def transpose(table: Iterable[Iterable[_T]]) -> List[List[_T]]:
    return list(map(list, zip(*table)))


def transpose_str(table: List[str]) -> List[str]:
    return list(map("".join, zip(*table)))


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
# N, M = map(int, input().split())
# A = list(map(int, input().split()))
# AB: List[Tuple[int, int]] = [tuple(map(int, input().split())) for _ in range(N)]
# N, *A = map(int, open(0).read().split())


if __name__ == "__main__":
    import doctest

    doctest.testmod()
