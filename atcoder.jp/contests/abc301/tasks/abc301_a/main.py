N = int(input())
S = input()


def solve():
    t = S.count("T")
    a = S.count("A")

    if t == a:
        if S[-1] == "A":
            return "T"
        return "A"

    if a < t:
        return "T"
    return "A"


print(solve())
