from itertools import combinations

N = int(input())
D = list(map(int, input().split()))

ans = sum(x * y for x, y in combinations(D, 2))
print(ans)
