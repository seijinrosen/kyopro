from typing import List, Tuple

N = int(input())
AB: List[Tuple[int, int]] = [tuple(map(int, input().split())) for _ in range(N - 1)]


G: List[List[int]] = [[] for _ in range(N)]
for a, b in AB:
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)


ans = N - 1 in map(len, G)


print("Yes" if ans else "No")
