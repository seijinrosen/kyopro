from itertools import combinations

A, B, C, D = map(int, input().split())

total = sum([A, B, C, D])
ans = any(
    sum(comb) * 2 == total for r in (1, 2, 3) for comb in combinations([A, B, C, D], r)
)

print("Yes" if ans else "No")
