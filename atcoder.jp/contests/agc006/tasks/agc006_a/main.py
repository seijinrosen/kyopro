def tails(s: str) -> "list[str]":
    return [s[i:] for i in range(len(s) + 1)]


N = int(input())
S = input()
T = input()

ans = next(N + i for i, tail in enumerate(tails(S)) if T.startswith(tail))
print(ans)
