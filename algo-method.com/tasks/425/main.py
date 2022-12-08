import sys

sys.setrecursionlimit(10**9)


def func(x: int) -> int:
    if x == 0:
        return 0
    if x == 1:
        return 1
    return func(x - 1) + func(x - 2)


print(func(int(input())))
