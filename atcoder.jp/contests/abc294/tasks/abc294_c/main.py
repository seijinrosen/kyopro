from collections import deque
from typing import List

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


queA = deque(A)
queB = deque(B)
ansA: List[int] = []
ansB: List[int] = []
i = 0

while queA or queB:
    i += 1

    if not queA:
        ansB.append(i)
        queB.popleft()
    elif not queB:
        ansA.append(i)
        queA.popleft()
    elif queA[0] < queB[0]:
        ansA.append(i)
        queA.popleft()
    else:
        ansB.append(i)
        queB.popleft()


print(*ansA)
print(*ansB)
