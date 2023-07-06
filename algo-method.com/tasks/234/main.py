N, *A = map(int, open(0).read().split())


def is_prime(x: int) -> bool:
    if x <= 1:
        return False
    return all(x % i != 0 for i in range(2, int(x**0.5) + 1))


def solve() -> int:
    return sum(map(is_prime, A))


print(solve())
