def int2bin(number: int, width: int) -> str:
    return bin(number)[2:].zfill(width)


def main() -> None:
    N = int(input())

    ans = int2bin(N, 10)

    print(ans)


main()
