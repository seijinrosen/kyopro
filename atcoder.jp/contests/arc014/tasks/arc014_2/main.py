N = int(input())
W = [input() for _ in range(N)]


def solve() -> str:
    used_words = {W[0]}

    for i in range(1, N):
        if W[i][0] != W[i - 1][-1] or W[i] in used_words:
            return "LOSE" if i % 2 == 0 else "WIN"
        used_words.add(W[i])

    return "DRAW"


print(solve())
