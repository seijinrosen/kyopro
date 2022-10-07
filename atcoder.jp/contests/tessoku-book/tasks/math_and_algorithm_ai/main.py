from itertools import accumulate


def input_int_list() -> "list[int]":
    return list(map(int, input().split()))


def input_int_pair_list(n: int) -> "list[tuple[int, int]]":
    return [tuple(map(int, input().split())) for _ in range(n)]


def main() -> None:
    _N, Q = input_int_list()
    A = input_int_list()
    LR = input_int_pair_list(Q)

    acc = [0, *accumulate(A)]
    ans = [acc[r] - acc[l - 1] for l, r in LR]

    print(*ans, sep="\n")


main()
