from typing import Set

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]


def dfs(i: int, j: int, st: Set[int]) -> int:
    a = A[i][j]

    if a in st:
        return 0

    if i == H - 1 and j == W - 1:
        return 1

    new_st = st.union({a})

    ret = 0
    if j + 1 < W:
        ret += dfs(i, j + 1, new_st)
    if i + 1 < H:
        ret += dfs(i + 1, j, new_st)

    return ret


ans = dfs(0, 0, set())


print(ans)
