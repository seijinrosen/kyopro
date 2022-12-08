import sys

sys.setrecursionlimit(10**9)


A, B = map(int, input().split())


def func(x: int) -> int:
    if x == A:
        return A
    return func(x - 1) + x


print(func(B))
