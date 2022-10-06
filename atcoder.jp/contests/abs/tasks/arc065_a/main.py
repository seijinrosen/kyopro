from typing import Union

CANDIDATES = ("dream", "dreamer", "erase", "eraser")
REVERSED_CANDIDATES = tuple(s[::-1] for s in CANDIDATES)


def yes_no(b: Union[bool, int]) -> str:
    return "YES" if b else "NO"


def main() -> None:
    S = input()

    s = S[::-1]

    while s:
        for candidate in REVERSED_CANDIDATES:
            if s.startswith(candidate):
                s = s[len(candidate) :]
                break
        else:
            ans = False
            break
    else:
        ans = True

    print(yes_no(ans))


main()
