from itertools import product

H, W = map(int, input().split())
S = [input() for _ in range(H)]


ans = sum(
    (j + 1 < W and S[i][j + 1] == ".") + (i + 1 < H and S[i + 1][j] == ".")
    for i, j in product(range(H), range(W))
    if S[i][j] == "."
)


print(ans)
