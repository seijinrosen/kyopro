S, c = open(0).read().split()


def solve() -> bool:
    return c in S


print("Yes" if solve() else "No")
