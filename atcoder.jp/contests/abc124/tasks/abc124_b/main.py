from itertools import accumulate

N = int(input())
H = list(map(int, input().split()))

acc = accumulate(H, max)
ans = sum(x <= h for x, h in zip(acc, H))

print(ans)
