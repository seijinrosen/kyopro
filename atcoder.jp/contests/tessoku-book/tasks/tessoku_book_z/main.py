from typing import Union


def is_prime(x: int) -> bool:
    return all(x % i != 0 for i in range(2, int(x**0.5) + 1))


def yes_no(b: Union[bool, int]) -> str:
    return "Yes" if b else "No"


Q = int(input())
X = [int(input()) for _ in range(Q)]

ans = map(is_prime, X)
print(*map(yes_no, ans), sep="\n")
