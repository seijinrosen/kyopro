from typing import List


def divisors(n: int) -> List[int]:
    """約数列挙
    >>> divisors(12)
    [1, 2, 3, 4, 6, 12]
    >>> divisors(827847039317)
    [1, 909859, 909863, 827847039317]
    """
    res: list[int] = []
    for i in range(1, n + 1):
        if n < i * i:
            break
        if n % i == 0:
            res.append(i)
            if i * i != n:
                res.append(n // i)
    return sorted(res)


N = int(input())
print(*divisors(N), sep="\n")
