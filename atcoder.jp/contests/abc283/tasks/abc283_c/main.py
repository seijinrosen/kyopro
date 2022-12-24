from collections import deque

que = deque(input())
ans = 0

while que:
    v = que.popleft()
    if v == "0" and que and que[0] == "0":
        que.popleft()
    ans += 1

print(ans)
