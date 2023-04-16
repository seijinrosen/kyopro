from operator import eq

# 標準入力から値を受け取る
# S: str 型
S = input()
# T: str 型
T = input()

# 受け取った値を利用してコードを書いてください
ans = "Bad" if 4 <= sum(map(eq, S, T)) else "Good"


print(ans)
