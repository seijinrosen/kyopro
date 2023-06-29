C, c = input().split()


def solve() -> bool:
    return C.lower() == c


print("Yes" if solve() else "No")
