def is_odd(n: int) -> bool:
    return n % 2 == 1


def input_int_list() -> "list[int]":
    return list(map(int, input().split()))


def main() -> None:
    A, B = input_int_list()

    ans = "Odd" if is_odd(A * B) else "Even"
    print(ans)


main()
