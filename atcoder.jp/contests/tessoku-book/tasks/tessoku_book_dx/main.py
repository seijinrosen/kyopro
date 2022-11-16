from typing import List

S = input()

stack: List[int] = []

for i, s in enumerate(S, start=1):
    if s == "(":
        stack.append(i)
    elif s == ")":
        print(stack.pop(), i)
