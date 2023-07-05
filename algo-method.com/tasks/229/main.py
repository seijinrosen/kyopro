S = input()
T = input()


def solve() -> bool:
    return T in S


print("Yes" if solve() else "No")
