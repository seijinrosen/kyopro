S = input()


def solve() -> int:
    return int("".join(ch for ch in S if ch.isdigit()))


print(solve())
