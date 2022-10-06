def main() -> None:
    N = int(input())
    D = [int(input()) for _ in range(N)]

    ans = len(set(D))

    print(ans)


main()
