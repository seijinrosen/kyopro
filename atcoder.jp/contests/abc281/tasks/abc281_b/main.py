def cond2(s: str) -> bool:
    if 6 < len(s):
        return False
    try:
        return 100000 <= int(s) <= 999999
    except ValueError:
        return False


S = input()

ans = all([S[0].isupper(), cond2(S[1:-1]), S[-1].isupper()])
print("Yes" if ans else "No")
