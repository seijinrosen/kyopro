# 標準入力から値を受け取る
# age: int 型
age = int(input())

# 受け取った値を利用してコードを書いてください
if age < 15:
    print("child")
elif age < 65:
    print("working-age")
else:
    print("senior")
