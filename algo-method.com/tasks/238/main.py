L, R = map(int, input().split())


def is_palindrome(s: str) -> bool:
    return s[::-1] == s


def solve() -> int:
    return sum(map(is_palindrome, map(str, range(L, R + 1))))


print(solve())
