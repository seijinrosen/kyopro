from itertools import product

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


def solve() -> int:
    return sum(a > b for a, b in product(A, B))


print(solve())
