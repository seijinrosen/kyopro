K = int(input())


def solve() -> int:
    cnt = 0

    for a in range(1, K + 1):
        for b in range(1, K + 1):
            if K < a * b:
                break

            for c in range(1, K + 1):
                if K < a * b * c:
                    break

                cnt += 1

    return cnt


print(solve())
