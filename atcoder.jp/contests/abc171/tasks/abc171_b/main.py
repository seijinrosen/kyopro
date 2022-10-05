def input_int_list() -> "list[int]":
    return list(map(int, input().split()))


def main() -> None:
    _N, K = input_int_list()
    P = input_int_list()

    ans = sum(sorted(P)[:K])
    print(ans)


main()
