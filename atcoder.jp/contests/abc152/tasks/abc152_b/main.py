def main() -> None:
    A, B = input().split()

    ans = min(A * int(B), B * int(A))

    print(ans)


main()
