def int2bin(number: int, width: int) -> str:
    return bin(number)[2:].zfill(width)


X = list(map(int, input().split()))


def get_square(bin_x: str, j: int) -> str:
    if bin_x[2 * j] == "0" and bin_x[2 * j + 1] == "0":
        return "."
    if bin_x[2 * j] == "0" and bin_x[2 * j + 1] == "1":
        return "o"
    return "x"


def get_line(x: int) -> str:
    bin_x = int2bin(x, 16)
    return "".join(get_square(bin_x, j) for j in range(8))


ans = map(get_line, X)
print(*ans, sep="\n")
