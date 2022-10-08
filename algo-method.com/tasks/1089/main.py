def solve(n: int) -> str:
    ret = ""
    if n % 4 == 0:
        ret += "Fizz"
    if n % 6 == 0:
        ret += "Buzz"
    return ret if ret else str(n)


def main() -> None:
    N = int(input())

    ans = map(solve, range(1, N + 1))

    print(*ans, sep="\n")


main()
