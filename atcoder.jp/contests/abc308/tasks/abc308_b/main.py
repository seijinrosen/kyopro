N, M = map(int, input().split())
C = input().split()
D = input().split()
P = list(map(int, input().split()))


def solve() -> int:
    prices = {d: p for d, p in zip(D, P[1:])}
    return sum(prices.get(c, P[0]) for c in C)


print(solve())
