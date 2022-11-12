N = int(input())
S = [input() for _ in range(N)]

st = set()

for s in S:
    if s[0] not in {"H", "D", "C", "S"}:
        ans = False
        break
    if s[1] not in {"A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"}:
        ans = False
        break
    if s in st:
        ans = False
        break
    st.add(s)
else:
    ans = True

print("Yes" if ans else "No")
