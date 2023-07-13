H, W = map(int, input().split())
S = [input().split() for _ in range(H)]


def solve() -> str:
    for h in range(H):
        for w in range(W):
            if S[h][w] == "snuke":
                return chr(ord("A") + w) + str(h + 1)

    return ""


print(solve())
