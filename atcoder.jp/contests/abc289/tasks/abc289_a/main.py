S = input()


def flip(ch: str) -> str:
    if ch == "0":
        return "1"
    return "0"


ans = "".join(map(flip, S))


print(ans)
