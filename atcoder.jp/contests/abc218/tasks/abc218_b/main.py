from string import ascii_lowercase


# input functions --------------------------------------------------------------
def input_int_list() -> "list[int]":
    return list(map(int, input().split()))


def main() -> None:
    P = input_int_list()

    ans = [ascii_lowercase[p - 1] for p in P]
    print(*ans, sep="")


main()
