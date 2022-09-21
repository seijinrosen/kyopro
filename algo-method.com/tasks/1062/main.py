def yes_no(b: bool) -> str:
    return "Yes" if b else "No"


A, M = map(int, input().split())

ans = A & M == M
print(yes_no(ans))
