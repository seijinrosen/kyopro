from typing import List, Set

# 標準入力から値を受け取る
# S: str 型
S = input()

# 受け取った値を利用してコードを書いてください
ans: List[str] = []
st: Set[str] = set()
for ch in S:
    ans.append("*" if ch in st else ch)
    st.add(ch)


print("".join(ans))
