poll_info = [90, 60, 240, 30, 180]

# ここに poll_info を加工するコードを書いてください
total = sum(poll_info)
for i, x in enumerate(poll_info):
    poll_info[i] = x * 100 // total

# poll_info を出力
print(poll_info)
