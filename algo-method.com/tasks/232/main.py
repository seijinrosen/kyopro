from itertools import product

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


def solve() -> int:
    return sum(a + b == K for a, b in product(A, B))


print(solve())
