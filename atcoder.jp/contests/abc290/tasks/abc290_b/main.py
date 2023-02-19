from typing import List

N, K = map(int, input().split())
S = input()


ans: List[str] = []
now = 0

for ch in S:
    if ch == "x" or K <= now:
        ans.append("x")
    else:
        ans.append("o")
        now += 1


print("".join(ans))
