N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


def solve() -> bool:
    a_gen = iter(sorted(A))

    for b in sorted(B):
        while True:
            try:
                a = next(a_gen)
            except StopIteration:
                return False

            if b <= a:
                break

    return True


print("YES" if solve() else "NO")
