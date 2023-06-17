N, V, *A = map(int, open(0).read().split())


def solve() -> bool:
    return V in A


print("Yes" if solve() else "No")
