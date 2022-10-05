def main() -> None:
    S = [input() for _ in range(3)]

    contests = {"ABC", "ARC", "AGC", "AHC"}
    ans = contests - set(S)

    print(*ans)


main()
