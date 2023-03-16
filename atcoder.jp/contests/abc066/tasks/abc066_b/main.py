S = input()


def is_even_string(s: str) -> bool:
    if len(s) % 2 == 1:
        return False

    x = len(s) // 2
    return s[:x] == s[x:]


ans = 0
for i in range(1, len(S)):
    s = S[:-i]
    if is_even_string(s):
        ans = len(s)
        break


print(ans)
