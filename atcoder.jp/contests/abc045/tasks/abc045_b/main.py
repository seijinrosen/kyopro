from collections import deque

A = deque(input())
B = deque(input())
C = deque(input())


now = A.popleft()

while True:
    if now == "a":
        x = A
    elif now == "b":
        x = B
    else:
        x = C

    if not x:
        break

    now = x.popleft()


print(now.upper())
