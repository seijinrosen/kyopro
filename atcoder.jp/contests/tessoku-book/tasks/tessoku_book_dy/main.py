from collections import deque

N, X = map(int, input().split())
A = list(input())

que = deque([X - 1])
A[X - 1] = "@"

while que:
    pos = que.popleft()

    if 1 <= pos and A[pos - 1] == ".":
        A[pos - 1] = "@"
        que.append(pos - 1)

    if pos + 1 < N and A[pos + 1] == ".":
        A[pos + 1] = "@"
        que.append(pos + 1)

ans = "".join(A)
print(ans)
