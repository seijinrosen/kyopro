from typing import List

N = int(input())
S = map(int, input())
T = map(int, input())

ans: List[int] = []
inc = 0

for s, t in reversed(list(zip(S, T))):
    now = inc + s + t
    if 1 < now:
        inc = 1
        now -= 2
    else:
        inc = 0
    ans.append(now)

print(*reversed(ans), sep="")
