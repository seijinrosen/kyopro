from itertools import count

N = int(input())
H = map(int, input().split())

ans = max(zip(H, count(start=1)))
print(ans[1])
