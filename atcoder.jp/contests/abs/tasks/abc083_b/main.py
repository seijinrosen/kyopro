def sum_of_each_digit(i: int) -> int:
    return sum(map(int, str(i)))


def input_int_list() -> "list[int]":
    return list(map(int, input().split()))


def main() -> None:
    N, A, B = input_int_list()

    ans = sum(i for i in range(1, N + 1) if A <= sum_of_each_digit(i) <= B)
    print(ans)


main()
