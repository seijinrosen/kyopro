K = int(input())
S = input()


def solve() -> str:
    if len(S) <= K:
        return S
    return S[:K] + "..."


ans = solve()


print(ans)
