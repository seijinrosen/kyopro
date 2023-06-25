N, X, *A = map(int, open(0).read().split())


def solve() -> bool:
    st = set(A)
    return any(a - X in st for a in A)


print("Yes" if solve() else "No")
