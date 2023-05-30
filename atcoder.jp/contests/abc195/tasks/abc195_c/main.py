N = int(input())


def solve() -> int:
    return sum(
        [
            max(0, N - 999),
            max(0, N - 999_999),
            max(0, N - 999_999_999),
            max(0, N - 999_999_999_999),
            max(0, N - 999_999_999_999_999),
        ]
    )


print(solve())
