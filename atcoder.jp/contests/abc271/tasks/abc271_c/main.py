from collections import deque
from itertools import groupby


def run_length_encoding(lst: "list[int]") -> "list[tuple[int, int]]":
    return [(k, len(list(g))) for k, g in groupby(lst)]


N = int(input())
A = list(map(int, input().split()))

A.sort()
run_length = run_length_encoding(A)

dup = 0
for k, v in run_length:
    dup += v - 1

que = deque(k for k, _ in run_length)
now = 0

while que or dup:
    if que and que[0] == now + 1:
        now = que.popleft()
    elif 2 <= dup:
        dup -= 2
        now += 1
    elif dup == 1 and que:
        dup = 0
        que.pop()
        now += 1
    elif 2 <= len(que):
        que.pop()
        que.pop()
        now += 1
    else:
        break

print(now)
