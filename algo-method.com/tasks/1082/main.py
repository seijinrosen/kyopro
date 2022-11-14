from typing import Set


def int2bitset(n: int) -> Set[int]:
    """
    >>> int2bitset(13)
    {0, 2, 3}
    >>> int2bitset(1)
    {0}
    """
    return {i for i, x in enumerate(reversed(bin(n)[2:])) if x == "1"}


N, X = map(int, input().split())
A = list(map(int, input().split()))

ans = sum(A[i] for i in int2bitset(X))
print(ans)
