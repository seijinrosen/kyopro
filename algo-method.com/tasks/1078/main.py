def input_int_list() -> "list[int]":
    return list(map(int, input().split()))


def main() -> None:
    N, X = input_int_list()

    ans = sum(0 < 1 << i & X for i in range(N))

    print(ans)


main()
