S = input()


def is_palindrome(s: str) -> bool:
    return s[::-1] == s


def solve() -> bool:
    return is_palindrome(S)


print("Yes" if solve() else "No")
