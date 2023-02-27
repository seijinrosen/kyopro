S = input()


ans = 0
for i, ch in enumerate(S, start=1):
    if ch.isupper():
        ans = i
        break


print(ans)
