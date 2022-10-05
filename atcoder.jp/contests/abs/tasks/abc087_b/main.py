from itertools import product


def main() -> None:
    A = int(input())
    B = int(input())
    C = int(input())
    X = int(input())

    ans = sum(
        500 * a + 100 * b + 50 * c == X
        for a, b, c in product(range(A + 1), range(B + 1), range(C + 1))
    )

    print(ans)


main()
