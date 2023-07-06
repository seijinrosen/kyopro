from typing import List, Tuple

N, *A = map(int, open(0).read().split())


def func(lst: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    if len(lst) <= 2:
        return lst

    return func(
        [max(lst[i], lst[i + 1], key=lambda x: x[1]) for i in range(0, len(lst), 2)]
    )


def solve() -> int:
    return min(func([(i, a) for i, a in enumerate(A, 1)]), key=lambda x: x[1])[0]


print(solve())
