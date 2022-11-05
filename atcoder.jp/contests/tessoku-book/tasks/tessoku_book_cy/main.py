from typing import List


def eratosthenes(n: int) -> List[int]:
    """N 以下の素数
    >>> eratosthenes(20)
    [2, 3, 5, 7, 11, 13, 17, 19]
    """
    deleted = [False] * (n + 1)
    deleted[0] = deleted[1] = True
    for i in range(int(n**0.5) + 1):
        if deleted[i]:
            continue
        for j in range(i * 2, n + 1, i):
            deleted[j] = True
    return [i for i, b in enumerate(deleted) if not b]


N = int(input())

ans = eratosthenes(N)
print(*ans, sep="\n")
