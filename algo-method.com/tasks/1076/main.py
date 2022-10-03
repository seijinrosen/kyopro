# input functions --------------------------------------------------------------
def input_int_list() -> "list[int]":
    return list(map(int, input().split()))


def main() -> None:
    _N, _K = input_int_list()
    V = input_int_list()

    ans = sum(1 << v for v in V)
    print(ans)


main()
