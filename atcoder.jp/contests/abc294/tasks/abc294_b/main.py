from string import ascii_uppercase

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]


def convert(a: int) -> str:
    if a == 0:
        return "."
    return ascii_uppercase[a - 1]


ans = ["".join(map(convert, row)) for row in A]


print(*ans, sep="\n")
