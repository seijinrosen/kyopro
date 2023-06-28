N = int(input())


def is_prime(x: int) -> bool:
    if x <= 1:
        return False
    return all(x % i != 0 for i in range(2, int(x**0.5) + 1))


def solve() -> bool:
    return is_prime(N)


print("Yes" if solve() else "No")
