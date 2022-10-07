from itertools import product


def input_int_list() -> "list[int]":
    return list(map(int, input().split()))


def main() -> None:
    N, K = input_int_list()

    ans = sum(1 <= K - i - j <= N for i, j in product(range(1, N + 1), repeat=2))

    print(ans)


main()
