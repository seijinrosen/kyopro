from typing import Set

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
QUERIES = [map(int, input().split()) for _ in range(Q)]

current_value = -1
b = [0] * N
changed: Set[int] = set()

for query in QUERIES:
    q = next(query)

    if q == 1:
        x = next(query)

        current_value = x
        changed: Set[int] = set()

    elif q == 2:
        i, x = query

        if current_value == -1:
            A[i - 1] += x
        else:
            if i - 1 in changed:
                b[i - 1] += x
            else:
                b[i - 1] = x
            changed.add(i - 1)

    elif q == 3:
        i = next(query)

        if current_value == -1:
            print(A[i - 1])
        else:
            if i - 1 in changed:
                print(current_value + b[i - 1])
            else:
                print(current_value)
