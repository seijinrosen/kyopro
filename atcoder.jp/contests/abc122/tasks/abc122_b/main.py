S = input()


def solve() -> int:
    ans = 0
    now = 0
    st = {"A", "C", "G", "T"}

    for ch in S:
        if ch in st:
            now += 1
        else:
            now = 0
        ans = max(ans, now)

    return ans


print(solve())
