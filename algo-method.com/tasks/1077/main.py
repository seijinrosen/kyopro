def main() -> None:
    N = int(input())

    ans = sum(1 << i for i in range(N))
    print(ans)


main()
