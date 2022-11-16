from heapq import heappop, heappush
from typing import List

Q = int(input())
QUERIES = [map(int, input().split()) for _ in range(Q)]

heap: List[int] = []

for query in QUERIES:
    q = next(query)

    if q == 1:
        x = next(query)
        heappush(heap, x)

    elif q == 2:
        print(heap[0])

    elif q == 3:
        heappop(heap)
