S = input()


def solve() -> bool:
    if S.find("B") % 2 == S.rfind("B") % 2:
        return False

    return S.find("R") < S.find("K") < S.rfind("R")


print("Yes" if solve() else "No")
