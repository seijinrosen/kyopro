from typing import List

N = int(input())
S = input()

is_bracketed = False
ans: List[str] = []

for c in S:
    ans.append("." if c == "," and not is_bracketed else c)
    if c == '"':
        is_bracketed = not is_bracketed

print("".join(ans))
