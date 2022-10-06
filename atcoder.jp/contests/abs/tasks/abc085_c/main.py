def input_int_list() -> "list[int]":
    return list(map(int, input().split()))


def main() -> None:
    N, Y = input_int_list()

    ans = next(
        (
            (i, j, N - i - j)
            for i in range(N + 1)
            for j in range(N - i + 1)
            if 10000 * i + 5000 * j + 1000 * (N - i - j) == Y
        ),
        (-1, -1, -1),
    )

    print(*ans)


main()
