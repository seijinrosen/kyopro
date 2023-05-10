A, V, B, W, T = map(int, open(0).read().split())


def solve() -> bool:
    return abs(A - B) <= (V - W) * T


print("YES" if solve() else "NO")
