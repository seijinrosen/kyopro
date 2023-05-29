S = input()


def solve() -> bool:
    try:
        return "F" in S[S.index("C") + 1 :]
    except ValueError:
        return False


print("Yes" if solve() else "No")
