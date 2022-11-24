from itertools import combinations

N = int(input())
A = map(int, input().split())

ans = max(map(sum, combinations(A, 2)))
print(ans)
