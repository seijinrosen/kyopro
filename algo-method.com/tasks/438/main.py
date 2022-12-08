import sys

sys.setrecursionlimit(10**9)


N, X, *A = map(int, open(0).read().split())

memo = [[-1] * (X + 1) for _ in range(N + 1)]


def func(i: int, j: int) -> int:
    if memo[i][j] != -1:
        pass
    elif i == 0:
        memo[i][j] = j == 0
    else:
        memo[i][j] = (A[i - 1] <= j and func(i - 1, j - A[i - 1])) or func(i - 1, j)
    return memo[i][j]


print("Yes" if func(N, X) else "No")
