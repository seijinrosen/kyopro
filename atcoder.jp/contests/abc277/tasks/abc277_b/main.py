N = int(input())
S = [input() for _ in range(N)]


def pred(s: str) -> bool:
    return s[0] in "HDCS" and s[1] in "A23456789TJQK"


ans = all(map(pred, S)) and len(set(S)) == N
print("Yes" if ans else "No")
