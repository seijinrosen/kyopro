N, *S = open(0).read().split()


def is_palindrome(s: str) -> bool:
    return s == s[::-1]


def solve() -> int:
    return sum(map(is_palindrome, S))


print(solve())
