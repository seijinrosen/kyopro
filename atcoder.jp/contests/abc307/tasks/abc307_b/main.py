from itertools import permutations


def is_palindrome(s: str) -> bool:
    return s[::-1] == s


N, *S = open(0).read().split()


def solve() -> bool:
    return any(map(is_palindrome, map("".join, permutations(S, 2))))


print("Yes" if solve() else "No")
