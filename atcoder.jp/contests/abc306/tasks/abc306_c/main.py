from typing import List

N, *A = map(int, open(0).read().split())


def solve() -> List[int]:
    lst: List[List[int]] = [[] for _ in range(N)]
    for i, a in enumerate(A, 1):
        lst[a - 1].append(i)

    return list(map(lambda x: x[0], sorted(enumerate(lst, 1), key=lambda x: x[1][1])))


print(*solve())
