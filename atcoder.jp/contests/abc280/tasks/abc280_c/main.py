S = input()
T = input()

i = 1
for s, t in zip(S, T):
    if s != t:
        ans = i
        break
    i += 1

print(i)
