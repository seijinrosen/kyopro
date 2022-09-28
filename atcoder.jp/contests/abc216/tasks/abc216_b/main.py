from typing import Union


def yes_no(b: Union[bool, int]) -> str:
    return "Yes" if b else "No"


N = int(input())
ST: "list[tuple[str, str]]" = [tuple(input().split()) for _ in range(N)]

ans = len(set(ST)) != N
print(yes_no(ans))
