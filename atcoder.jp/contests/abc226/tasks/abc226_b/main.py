N = int(input())
L = [input() for _ in range(N)]


def solve() -> int:
    return len(set(L))


print(solve())
