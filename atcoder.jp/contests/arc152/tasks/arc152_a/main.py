N, L, *A = map(int, open(0).read().split())


def solve() -> bool:
    remaining = L

    for a in A:
        if a == 2 and remaining < 2:
            return False
        remaining -= 1 + a

    return True


print("Yes" if solve() else "No")
