from itertools import product
from typing import Set

H, W = map(int, input().split())
C = [list(input()) for _ in range(H)]


for i, j in product(range(H), range(W)):
    if C[i][j] != ".":
        continue

    st: Set[str] = set()
    if 0 <= i - 1:
        st.add(C[i - 1][j])
    if 0 <= j - 1:
        st.add(C[i][j - 1])
    if j + 1 < W:
        st.add(C[i][j + 1])
    if i + 1 < H:
        st.add(C[i + 1][j])

    if "1" not in st:
        x = "1"
    elif "2" not in st:
        x = "2"
    elif "3" not in st:
        x = "3"
    elif "4" not in st:
        x = "4"
    else:
        x = "5"

    C[i][j] = x


for row in C:
    print("".join(row))
