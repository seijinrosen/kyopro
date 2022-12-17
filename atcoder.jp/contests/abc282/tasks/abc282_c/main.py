from typing import List

N = int(input())
S = input()

is_kukurare = False

ans: List[str] = []

for c in S:
    if not is_kukurare and c == ",":
        ans.append(".")
    else:
        ans.append(c)

    if c == '"':
        is_kukurare = not is_kukurare

print("".join(ans))
