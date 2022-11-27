from itertools import product
from typing import Callable, Iterable, Iterator, Tuple, TypeVar, Union

_T = TypeVar("_T")
_S = TypeVar("_S")


def accumulate_initial(
    iterable: Iterable[_S], func: Callable[[_T, _S], _T], *, initial: _T
) -> Iterator[_T]:
    # https://docs.python.org/ja/3/library/itertools.html#itertools.accumulate
    total = initial
    yield total
    for element in iter(iterable):
        total = func(total, element)
        yield total


def bitset(n: int) -> Iterator[Tuple[int, ...]]:
    for bits in product((0, 1), repeat=n):
        yield bits


def bool2score(x: Union[bool, int]) -> int:
    return 2 * x - 1


def is_natural(n: int) -> bool:
    return 0 <= n


N = int(input())


def acc_func(x: int, y: int) -> int:
    return x + bool2score(y)


def bit2parentheses(bit: int) -> str:
    if bit:
        return "("
    return ")"


ans = [
    "".join(map(bit2parentheses, bits))
    for bits in bitset(N)
    if sum(bits) == N // 2
    if all(map(is_natural, accumulate_initial(bits, acc_func, initial=0)))
]

print(*reversed(ans), sep="\n")
