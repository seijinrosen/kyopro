def main() -> None:
    S = input()
    T = input()

    ans = sum(s != t for s, t in zip(S, T))
    print(ans)


main()
