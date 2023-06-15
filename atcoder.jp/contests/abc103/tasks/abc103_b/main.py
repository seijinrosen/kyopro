from collections import deque

S = input()
T = input()


def solve() -> bool:
    que = deque(S)

    for _ in range(len(que)):
        if "".join(que) == T:
            return True

        que.rotate()

    return False


print("Yes" if solve() else "No")
