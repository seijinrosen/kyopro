from typing import Union


def yes_no(b: Union[bool, int]) -> str:
    return "Yes" if b else "No"


N = int(input())
A = [int(x) - 1 for x in input().split()]

bucket = [False] * N

for a in A:
    if bucket[a]:
        ans = False
        break
    bucket[a] = True
else:
    ans = True

print(yes_no(ans))
