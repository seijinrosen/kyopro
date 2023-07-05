N, S, T = open(0).read().split()


def solve() -> int:
    return sum(s != t for s, t in zip(S, T))


print(solve())
