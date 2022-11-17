from typing import List, Tuple

N = int(input())
A = list(map(int, input().split()))

ans: List[int] = []
stack: List[Tuple[int, int]] = []

for d, Ad in enumerate(A, start=1):
    while stack:
        i, Ai = stack[-1]
        if Ai > Ad:
            ans.append(i)
            break
        else:
            stack.pop()
    else:
        ans.append(-1)

    stack.append((d, Ad))

print(*ans)
