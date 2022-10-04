def input_int_list() -> "list[int]":
    return list(map(int, input().split()))


def main() -> None:
    A = int(input())
    B, C = input_int_list()
    S = input()

    ans = A + B + C
    print(ans, S)


main()
