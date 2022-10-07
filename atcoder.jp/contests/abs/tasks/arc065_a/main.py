from typing import Union

CANDIDATES = ("dream", "dreamer", "erase", "eraser")
REVERSED_CANDIDATES = tuple(s[::-1] for s in CANDIDATES)


def yes_no(b: Union[bool, int]) -> str:
    return "YES" if b else "NO"


def solve(s: str) -> bool:
    while s:
        try:
            prefix = next(p for p in REVERSED_CANDIDATES if s.startswith(p))
        except StopIteration:
            return False
        s = s[len(prefix) :]
    return True


def main() -> None:
    S = input()

    ans = solve(S[::-1])

    print(yes_no(ans))


main()
