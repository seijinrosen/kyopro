from typing import List

A, B = map(int, input().split())

ans: List[int] = []

if A < B:
    for i in range(1, B + 1):
        ans.append(-i)
    for i in range(1, A):
        ans.append(i)
else:
    for i in range(1, A + 1):
        ans.append(i)
    for i in range(1, B):
        ans.append(-i)

ans.append(-sum(ans))
print(*ans)
