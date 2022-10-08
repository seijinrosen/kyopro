from itertools import product

N, M = map(int, input().split())

sets: "list[set[int]]" = [set() for _ in range(N)]

for _ in range(M):
    k, *lst = list(map(int, input().split()))
    for x, y in product(lst, repeat=2):
        sets[x - 1].add(y - 1)

ans = all(len(s) == N for s in sets)
print("Yes" if ans else "No")
