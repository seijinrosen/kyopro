from typing import Counter

S = input()


def solve() -> bool:
    if len(S) <= 2:
        return int(S) % 8 == 0 or int(S[::-1]) % 8 == 0

    counter = Counter(S)

    for i in range(104, 1000, 8):
        if not Counter(str(i)) - counter:
            return True

    return False


print("Yes" if solve() else "No")
