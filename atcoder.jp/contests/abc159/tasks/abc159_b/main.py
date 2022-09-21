S = input()


def is_palindrome(s: str) -> bool:
    return s == s[::-1]


def former(s: str) -> str:
    n = len(s)
    return s[: (n - 1 // 2)]


def latter(s: str) -> str:
    n = len(s)
    return s[(n + 3) // 2 - 1 :]


ok = all(map(is_palindrome, [S, former(S), latter(S)]))
ans = "Yes" if ok else "No"

print(ans)
