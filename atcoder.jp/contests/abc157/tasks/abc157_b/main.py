from typing import Iterable, List, TypeVar

_T = TypeVar("_T")


def transpose(table: Iterable[Iterable[_T]]) -> List[List[_T]]:
    return list(map(list, zip(*table)))


A = [list(map(int, input().split())) for _ in range(3)]
N = int(input())
B = [int(input()) for _ in range(N)]


def solve() -> bool:
    numbers = set(B)

    for row in A:
        if all(a in numbers for a in row):
            return True

    for col in transpose(A):
        if all(a in numbers for a in col):
            return True

    if all(a in numbers for a in [A[0][0], A[1][1], A[2][2]]):
        return True

    if all(a in numbers for a in [A[0][2], A[1][1], A[2][0]]):
        return True

    return False


print("Yes" if solve() else "No")
