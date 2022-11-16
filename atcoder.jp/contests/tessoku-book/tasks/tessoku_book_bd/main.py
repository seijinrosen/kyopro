from typing import Callable, Iterable, Iterator, List, Tuple, TypeVar

_T = TypeVar("_T")
_S = TypeVar("_S")


def accumulate_with_initial(
    iterable: Iterable[_S], func: Callable[[_T, _S], _T], initial: _T
) -> Iterator[_T]:
    # https://docs.python.org/ja/3/library/itertools.html#itertools.accumulate
    total = initial
    yield total
    for element in iter(iterable):
        total = func(total, element)
        yield total


N, Q = map(int, input().split())
S = input()
ABCD: List[Tuple[int, int, int, int]] = [
    tuple(map(int, input().split())) for _ in range(Q)
]

MOD = 2147483647
power100 = [pow(100, i, MOD) for i in range(N + 1)]

T = [ord(c) - ord("a") + 1 for c in S]
H = list(accumulate_with_initial(T, lambda x, y: (x * 100 + y) % MOD, initial=0))


def hash_value(l: int, r: int) -> int:
    return (H[r] - H[l - 1] * power100[r - l + 1]) % MOD


for a, b, c, d in ABCD:
    ans = hash_value(a, b) == hash_value(c, d)
    print("Yes" if ans else "No")
