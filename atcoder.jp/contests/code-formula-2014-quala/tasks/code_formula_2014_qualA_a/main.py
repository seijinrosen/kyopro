A = int(input())


def solve() -> bool:
    return any(i**3 == A for i in range(1, 101))


print("YES" if solve() else "NO")
