def is_palindrome(s: str) -> bool:
    return s[::-1] == s


print("YES" if is_palindrome(input()) else "NO")
