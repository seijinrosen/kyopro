N, S, T = open(0).read().split()


def is_similar(x: str, y: str) -> bool:
    if x == y:
        return True
    if x == "1" and y == "l":
        return True
    if x == "l" and y == "1":
        return True
    if x == "0" and y == "o":
        return True
    if x == "o" and y == "0":
        return True
    return False


def solve() -> bool:
    return all(map(is_similar, S, T))


print("Yes" if solve() else "No")
