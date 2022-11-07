from typing import List, Tuple

input_int_list = lambda: list(map(int, input().split()))

N, M = input_int_list()
AB: List[Tuple[int, int]] = [tuple(input_int_list()) for _ in range(M)]

cities: List[List[int]] = [[] for _ in range(N)]
for a, b in AB:
    cities[a - 1].append(b)
    cities[b - 1].append(a)

for city in cities:
    print(len(city), *sorted(city))
