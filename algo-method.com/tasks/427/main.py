import sys

sys.setrecursionlimit(10**9)


N, X, *A = map(int, open(0).read().split())


def func(i: int, j: int) -> bool:
    if i == 0:
        return j == 0
    flag = False
    if j >= A[i - 1] and func(i - 1, j - A[i - 1]):
        flag = True
    if func(i - 1, j):
        flag = True
    return flag


print("Yes" if func(N, X) else "No")
