def is_prime(x: int) -> bool:
    return all(x % i != 0 for i in range(2, int(x**0.5) + 1))


X = int(input())


def solve():
    for i in range(X, 10**7):
        if is_prime(i):
            return i


print(solve())
