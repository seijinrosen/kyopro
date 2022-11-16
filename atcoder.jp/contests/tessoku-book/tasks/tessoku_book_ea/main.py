from collections import Counter

N = int(input())
A = [int(input()) for _ in range(N)]

ans = sum(v * (v - 1) // 2 for v in Counter(A).values())
print(ans)
