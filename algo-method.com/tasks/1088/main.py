def input_int_list() -> "list[int]":
    return list(map(int, input().split()))


def main() -> None:
    SA, TA = input_int_list()
    SB, TB = input_int_list()

    ans = max(0, min(TA, TB) - max(SA, SB))

    print(ans)


main()
