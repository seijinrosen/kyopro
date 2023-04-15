# 標準入力から値を受け取る
# S: str 型
S = input()


# 受け取った値を利用してコードを書いてください
def convert(last_name: str, first_name: str) -> str:
    return first_name.lower()[0] + "_" + last_name.lower()


ans = convert(*S.split())


print(ans)
