def is_palindrome(s: str) -> bool:
    return s[::-1] == s


N = input()

ans = is_palindrome(N.rstrip("0"))
print("Yes" if ans else "No")
