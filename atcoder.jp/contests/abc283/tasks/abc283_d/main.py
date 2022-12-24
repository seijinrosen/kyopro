from collections import deque
from typing import Counter, Deque

S = input()

que: Deque[str] = deque()
counter: Counter[str] = Counter()

for c in S:
    if c == ")":
        while que:
            v = que.pop()
            if v == "(":
                break
            else:
                counter[v] -= 1
    elif c == "(":
        que.append(c)
    else:
        que.append(c)
        if counter[c] > 0:
            ans = False
            break
        counter[c] += 1
else:
    ans = True

print("Yes" if ans else "No")
