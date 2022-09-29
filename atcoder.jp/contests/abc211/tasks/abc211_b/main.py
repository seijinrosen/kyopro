from typing import Union


def yes_no(b: Union[bool, int]) -> str:
    return "Yes" if b else "No"


S = [input() for _ in range(4)]

ans = len(set(S)) == 4
print(yes_no(ans))
