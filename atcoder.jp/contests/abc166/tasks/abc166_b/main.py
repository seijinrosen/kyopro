from typing import Set

N, K = map(int, input().split())

st: Set[int] = set()

for _ in range(K):
    d = int(input())
    A = map(int, input().split())
    st.update(A)

ans = N - len(st)
print(ans)
