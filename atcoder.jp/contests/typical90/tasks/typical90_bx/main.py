from collections import deque

N, *A = map(int, open(0).read().split())


def solve() -> bool:
    total = sum(A)
    k = total // 10
    if 10 * k != total:
        return False

    que: deque[int] = deque()
    now = 0
    for a in A * 2:
        que.append(a)
        now += a
        while que and k < now:
            now -= que.popleft()
        if now == k and len(que) <= N:
            return True
    return False


print("Yes" if solve() else "No")
