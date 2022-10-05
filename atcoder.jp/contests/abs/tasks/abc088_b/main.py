def input_int_list() -> "list[int]":
    return list(map(int, input().split()))


def main() -> None:
    _N = int(input())
    A = input_int_list()

    A.sort(reverse=True)
    alice = sum(A[::2])
    bob = sum(A[1::2])

    ans = alice - bob
    print(ans)


main()
