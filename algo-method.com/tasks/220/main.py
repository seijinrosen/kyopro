N = int(input())


def is_ok(i: int) -> bool:
    if i % 2 == 0:
        return False
    if i % 3 == 0:
        return False
    if i % 5 == 0:
        return False
    return True


def solve() -> int:
    return sum(map(is_ok, range(1, N + 1)))


print(solve())
