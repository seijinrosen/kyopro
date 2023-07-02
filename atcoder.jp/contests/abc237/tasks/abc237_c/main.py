def is_palindrome(s: str) -> bool:
    return s[::-1] == s


S = input()


def solve() -> bool:
    l = len(S.lstrip("a"))

    if l == 0:
        return True

    if l < len(S.rstrip("a")):
        return False

    return is_palindrome(S.strip("a"))


print("Yes" if solve() else "No")
