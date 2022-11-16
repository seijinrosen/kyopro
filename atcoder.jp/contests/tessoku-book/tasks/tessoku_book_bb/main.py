from typing import Dict

Q = int(input())
QUERIES = [input().split() for _ in range(Q)]

D: Dict[str, int] = {}

for query in QUERIES:
    q = int(query[0])
    x = query[1]

    if q == 1:
        y = int(query[2])
        D[x] = y

    elif q == 2:
        print(D[x])
