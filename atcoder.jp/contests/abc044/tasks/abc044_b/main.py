from typing import Counter

W = input()


def solve() -> bool:
    return all(v % 2 == 0 for v in Counter(W).values())


print("Yes" if solve() else "No")
