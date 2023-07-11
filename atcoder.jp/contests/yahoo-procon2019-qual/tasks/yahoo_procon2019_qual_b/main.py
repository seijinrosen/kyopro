from typing import List

cities: List[List[int]] = [[] for _ in range(4)]
for _ in range(3):
    a, b = map(int, input().split())
    cities[a - 1].append(b - 1)
    cities[b - 1].append(a - 1)


def solve() -> bool:
    return all(len(c) <= 2 for c in cities)


print("YES" if solve() else "NO")
