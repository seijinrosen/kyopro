from collections import Counter

N, *A = map(int, open(0).read().split())


def solve() -> int:
    counter = Counter(A)
    return max(counter.keys(), key=lambda k: counter[k])


print(solve())
