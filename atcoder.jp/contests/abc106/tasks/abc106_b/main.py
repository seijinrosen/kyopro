from typing import List


def divisors(n: int) -> List[int]:
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


def solve() -> int:
    return sum(len(divisors(i)) == 8 for i in range(1, N + 1, 2))


print(solve())
