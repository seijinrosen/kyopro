from itertools import product

X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))


def solve() -> int:
    return sum(a + b == c for a, b, c in product(A, B, C))


print(solve())
