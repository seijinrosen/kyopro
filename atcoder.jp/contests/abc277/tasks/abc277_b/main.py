N = int(input())
S = [input() for _ in range(N)]


def cond1(s: str) -> bool:
    return s[0] in {"H", "D", "C", "S"}


def cond2(s: str) -> bool:
    return s[1] in {"A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"}


ans = all(map(cond1, S)) and all(map(cond2, S)) and len(set(S)) == N
print("Yes" if ans else "No")
