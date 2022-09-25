from typing import Union


def yes_no(b: Union[bool, int]) -> str:
    return "Yes" if b else "No"


X = list(map(int, input()))
P, Q = input().split()

user = {"o": 0, "g": 1, "u": 2}
permission = {"r": 4, "w": 2, "x": 1}

ans = X[user[P]] & permission[Q]
print(yes_no(ans))
