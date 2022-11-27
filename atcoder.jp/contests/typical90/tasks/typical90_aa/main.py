from typing import Set

N = int(input())
S = [input() for _ in range(N)]

st: Set[str] = set()

for i, s in enumerate(S, 1):
    if s not in st:
        st.add(s)
        print(i)
