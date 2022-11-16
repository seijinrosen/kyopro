from typing import List

Q = int(input())
QUERIES = [input().split() for _ in range(Q)]

stack: List[str] = []

for query in QUERIES:
    q = int(query[0])

    if q == 1:
        x = query[1]
        stack.append(x)

    elif q == 2:
        print(stack[-1])

    elif q == 3:
        stack.pop()
