def bin2int(b: str) -> int:
    return int(b, 2)


def main() -> None:
    N = input()

    ans = bin2int(N)

    print(ans)


main()
