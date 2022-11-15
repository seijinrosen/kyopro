X, Y = map(int, input().split())

x = X
y = Y
ans = [(x, y)]

while not (x == 1 and y == 1):
    if x < y:
        y -= x
    else:
        x -= y
    ans.append((x, y))

print(len(ans) - 1)
for xy in ans[::-1][1:]:
    print(*xy)
