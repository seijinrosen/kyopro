A, B, C, D = map(int, input().split())


def solve() -> int:
    cnt = 0
    blue = A
    red = 0

    while D * red < blue:
        cnt += 1
        blue += B
        red += C
        if 10**6 <= cnt:
            return -1

    return cnt


print(solve())
